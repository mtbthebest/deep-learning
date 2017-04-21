#!/usr/bin/env python

import numpy as np
import tensorflow as tf

W=tf.Variable([.3], tf.float32)
b=tf.Variable([-.3], tf.float32)

xrange = tf.placeholder(tf.float32)
linear_model = W * x + b
