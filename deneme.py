import tensorflow as tf

# TensorFlow'un GPU'yu görüp görmediğini kontrol edin
print("TensorFlow GPU support:", tf.test.is_built_with_cuda())
print("Available GPUs:", tf.config.list_physical_devices('GPU'))
