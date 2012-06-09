# -*- coding: utf-8 -*-
from pymongo import Connection
import random
from time import sleep
import datetime

db = Connection().mesh

arduinos = [0xCB]
pins = [14, 15, 16, 17, 18]

try:
    while True:
        millis = random.randint(500, 2000)
        sleep(millis/1000)

        infos = {}
        infos['arduino'] = arduinos[random.randint(0,len(arduinos)-1)]
        infos['pin'] = pins[random.randint(0,len(pins)-1)]
        infos['value'] = random.randint(0,255)
        infos['date'] = datetime.datetime.utcnow()
        info = db.mesh_captors.save(infos)
        print info, infos
except KeyboardInterrupt:
    exit(0)