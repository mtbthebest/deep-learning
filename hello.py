#!/usr/bin/env python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

hello = tf.constant('hello TensorFlow!', tf.string)
sess = tf.Session()
print sess.run(hello)

node = tf.constant(4.0, tf.float32)
print node
print sess.run(node)

node_add = tf.add(node, tf.constant(5.0))
print node_add
print sess.run(node_add)