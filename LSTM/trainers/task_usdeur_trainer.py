import numpy as np
from sklearn.preprocessing import MinMaxScaler
from model.model import Model


class TaskUsdEurTrainer():
    def __init__(self, model_path, spark_session, data_path="hdfs://hadoop-namenode:8020/data/task-usdeur/"):
        self.model_path = model_path
        self.spark_session = spark_session
        self.data_path = data_path
        self.scaler = MinMaxScaler()
        self.look_back = 1
        self.train_samples = 1500


    def train(self):
        data_hdfs =  self.spark_session.read.csv(self.data_path)
        dataset = np.array(data_hdfs.select("_c5").collect())
        print("dataset.shape: ", dataset.shape)

        #scale dataset
        dataset = self.scaler.fit_transform(dataset)

        #Split data to train/test set
        train = dataset[:self.train_samples]
        test = dataset[self.train_samples:]


        #Prepare data to training
        x_train, y_train = self.get_data(train, self.look_back)
        x_test, y_test = self.get_data(test, self.look_back)
        x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
        x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)
        print("x_train.shape: ", x_train.shape)
        print("x_test.shape: ", x_test.shape)

        print("TRAINING MODEL")
        model = Model().lstm_basic(x_train.shape[1])
        model.fit(x_train, y_train, epochs = 5, batch_size = 1, validation_data=(x_test, y_test))

        print("EVALUATE MODEL")
        model.evaluate(x_test, y_test, batch_size = 1)

        #save model
        model.save(self.model_path)


    def get_data(self, data, look_back):
        datax, datay = [], []
        for i in range(len(data) - look_back - 1):
            datax.append(data[i:(i + look_back), 0])
            datay.append(data[i + look_back, 0])
        return np.array(datax), np.array(datay)

