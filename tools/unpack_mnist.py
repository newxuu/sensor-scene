import cPickle, gzip, numpy
from scipy.misc import imsave
import os

f = gzip.open('../dataset/mnist.pkl.gz', 'rb')
train_set, valid_set = cPickle.load(f)
f.close()

for i in xrange(1000):
  img = train_set[0][i]
  label = train_set[1][i]
  imsave('../dataset/mnist/%s-%s.png' % (i, label), img)
