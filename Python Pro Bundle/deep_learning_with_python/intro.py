import theano
from theano import tensor 

a = tensor.dscalar() # declaring two symbolic floating-point scalars 
b = tensor.dscalar()
c = a + b # creating symbolic expression 
f = theano.function([a, b], c) # callable object taking in [a, b] and computes c
result = f(1.5, 2.5)
print(result)

import tensorflow as tf
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
add = tf.add(a, b)
sess = tf.Session()
binding = {a : 1.5, b : 2.5} # binding 1.5 to a and 2.5 to b
c = sess.run(add, feed_dict=binding)
print(c)


# Command Line: Finding where tensorflow is installed in your system
# python -c 'import os; import inspect; import tensorflow; print(os.path.dirname(inspect.getfile(tensorflow)))'

                                                                
                                                                
                                                                

                                                                
                                                                
                                                                