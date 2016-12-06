# -*- coding:utf-8 -*-

# TODO: logger
# TODO: clarify the img format. Must be the single channel as th. 
# TODO: fiting takes too much time

from __future__ import print_function

import os
import sys
sys.path.append('lib')

from itertools import izip
import classify
import stream as img_stream
import serial

model = classify.Classify(10)
imgGenerator = img_stream.camera(0)
ser = serial.Serial('mock')

scene = 0

while True:

  # check serial
  if ser.is_ready():
    cmd, payload = ser.get_payload()
    # fit the model
    if cmd == 0:
      sid = payload
      # fit 3 times
      for _, item in izip(xrange(3), imgGenerator):
        img, stamp = item
        model.fit_once(img, sid)

  # check scene
  tmp = model.predict(imgGenerator.next())
  if not tmp == scene:
    # feedback the scene id
    scene = tmp
    ser.send(1, scene)