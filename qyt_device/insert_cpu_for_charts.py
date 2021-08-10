#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djghomework.settings')
django.setup()
from qyt_device.models import Devicecpu, Devicedb
from random import randint
from time import sleep
from datetime import datetime

Devicecpu.objects.all().delete()

for i in range(50):
    record_time = datetime.now()
    for d in Devicedb.objects.all():
        cpu = randint(1, 100)
        c = Devicecpu(device=d, cpu_usage=cpu, record_datetime=record_time)
        c.save()
    sleep(1)
