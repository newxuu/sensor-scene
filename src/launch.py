# -*- coding:utf-8 -*-

from __future__ import print_function

import os
import sys
sys.path.append('lib')

from itertools import izip
import numpy as np
import classify
import stream as img_stream
import serial
from log import sys_logger as logger

model = classify.Classify(10)
streamFactory = img_stream.Stream()
imgGenerator = streamFactory.from_camera(0)
ser = serial.Serial('mock')

scene = 0

logger.info('lanuch successfully')

while True:

  # check serial
  if ser.is_ready():
    cmd, payload = ser.get_payload()
    # fit the model
    if cmd == 0:
      sid = payload
      logger.info('fitting sid = %d', sid)
      # fit 3 times
      for _, item in izip(xrange(3), imgGenerator):
        img, stamp = item
        model.fit_single(img, sid)

  # check scene
  img, stamp = imgGenerator.next()
  sid, sid_p = model.predict(img)
  logger.debug('predict sid = %s with %s chance', sid, sid_p)
  if not sid == scene:
    # feedback the scene id
    scene = sid
    ser.send(1, scene)