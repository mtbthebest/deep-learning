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
print [sess.run(node_add)]

a   = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print sess.run(adder_node, {a:[1,3], b: [2,4]})

W= tf.Variable([.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
init = tf.global_variables_initializer()
sess.run(init)
print sess.run(linear_model, {x:[1,2,3,4]})

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]})

fixW = tf.assign(W, [-1.0])
fixb = tf.assign(b, [1.0])
sess.run([fixW,fixb])
print sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]})

optimizer  = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)

for i in range(1000):
    sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

print sess.run([W,b])