import tensorrt as trt

import tensorflow as tf

print(tf.test.is_built_with_cuda())

print(tf.config.list_physical_devices('GPU'))