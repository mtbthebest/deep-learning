#!/usr/bin/env python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
x = tf.constant(1.0,name = 'x')
y = tf.Variable(initial_value = x+9, name = 'y')

model = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(model)
    print sess.run(y)

a = tf.placeholder(dtype = tf.float32)
b = tf.placeholder(dtype = tf.float32)
c = tf.multiply(a,b,name = 'c')

sess = tf.Session()
print sess.run(c, feed_dict = {a:2.0,b:5})