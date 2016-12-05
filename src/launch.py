# -*- coding:utf-8 -*-

from __future__ import print_function

import os
import sys
sys.path.append('lib')

import classify
import stream as img_stream

cor = classify.Classify(10)
imgGenerator = img_stream.local('../dataset/mnist')

for i in xrange(10):
  img, stamp = imgGenerator.next()
  print('fit in', img.shape, 1)  
  cor.fit_once(img, 1)
