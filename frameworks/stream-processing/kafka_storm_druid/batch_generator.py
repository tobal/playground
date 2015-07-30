#! /usr/bin/env python

import random
import datetime

for i in range(100):
    for name in ['szende', 'szundi', 'morgo', 'hapci', 'tudor', 'vidor', 'kuka']:
        number = random.randint(0, 1000)
        time = datetime.datetime.now().isoformat()
        data_record = {'name': name, 'number': number, 'timestamp': time}
        print(data_record)

