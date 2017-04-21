#!/usr/bin/env python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

hello = tf.constant('hello TensorFlow!')
sess = tf.Session()
print sess.run(hello)