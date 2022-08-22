import tensorflow as tf
from tensorflow.keras.layers import Flatten, Dense, Input, Conv1D, AveragePooling1D, BatchNormalization, Activation, Layer, Concatenate
k = tf.keras
kl = tf.keras.layers

def model(input_size=700, classes=256):
    input_shape = (input_size,1)
    input_w = kl.Input(shape=input_shape)
    
    x = kl.Conv1D(4, 1, kernel_initializer='he_uniform', padding='same')(input_w)
    x = kl.Activation('selu')(x)
    s = kl.Conv1D(4, 1, kernel_initializer='he_uniform', padding='same')(input_w)
    s = kl.Activation('selu')(s)
    x = kl.Subtract()([s, x])
    y = kl.Conv1D(4, 3, kernel_initializer='he_uniform', padding='same')(x)
    y = kl.Activation('selu')(y)
    z = kl.Conv1D(4, 3, kernel_initializer='he_uniform', padding='same')(x)
    z = kl.Activation('tanh')(z)
    w = kl.Multiply()([y,z])

    w = kl.Conv1D(4, 3, kernel_initializer='he_uniform', padding='same')(w)
    w = kl.BatchNormalization()(w)
    w = kl.Activation('selu')(w)
    w = kl.AveragePooling1D(2, strides=2)(w)
    w = kl.Conv1D(4, 3, kernel_initializer='he_uniform', padding='same')(w)
    w = kl.BatchNormalization()(w)
    w = kl.Activation('selu')(w)
    w = kl.AveragePooling1D(2, strides=2)(w)
    w = kl.Conv1D(4, 3, kernel_initializer='he_uniform', padding='same')(w)
    w = kl.BatchNormalization()(w)
    w = kl.Activation('selu')(w)
    w = kl.AveragePooling1D(2, strides=2)(w)
    w = kl.Conv1D(8, 3, kernel_initializer='he_uniform', padding='same')(w)
    w = kl.BatchNormalization()(w)
    w = kl.Activation('selu')(w)
    w = kl.AveragePooling1D(2, strides=2)(w)
    w = kl.Conv1D(8, 3, kernel_initializer='he_uniform', padding='same')(w)
    w = kl.BatchNormalization()(w)
    w = kl.Activation('selu')(w)
    w = kl.AveragePooling1D(2, strides=2)(w)
    w = kl.Flatten()(w)
    w = kl.Dense(20, kernel_initializer='he_uniform', activation='selu')(w)
    w = kl.Dense(20, kernel_initializer='he_uniform', activation='selu')(w)
    output = kl.Dense(classes)(w)
    return k.Model(input_w,output)
