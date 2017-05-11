#!/usr/bin/env python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

weights = tf.Variable(tf.random_normal([784,200],stddev=0.2), name ='weights')
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print sess.run(weights)
