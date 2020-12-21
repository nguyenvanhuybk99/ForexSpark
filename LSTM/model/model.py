from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM

class Model():
    def __init__(self):
        pass

    def lstm_basic(self, n_features):
        model = Sequential()
        model.add(LSTM(100, activation='relu', input_shape=(1, 1)))
        model.add(Dense(n_features))
        print(model.summary())
        model.compile(optimizer='adam', loss='mse')

        return model

