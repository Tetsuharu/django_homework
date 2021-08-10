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
from qyt_device.models import Devicecpu, Devicedb, DeviceSNMP, Devicetype, SNMPtype
from random import randint
from time import sleep

Devicecpu.objects.all().delete()
Devicedb.objects.all().delete()
Devicetype.objects.all().delete()
DeviceSNMP.objects.all().delete()
SNMPtype.objects.all().delete()

device_type_router = Devicetype(name='CSR1000v')
device_type_router.save()

snmp_type_router = SNMPtype(name='CPU Totol 5sec')
snmp_type_router.save()

device_snmp_router = DeviceSNMP(device_type=Devicetype.objects.get(name='CSR1000v'),
                                snmp_type=SNMPtype.objects.get(name='CPU Totol 5sec'),
                                oid='1.3.6.1.4.1.9.9.109.1.1.1.1.3.7'
                                )
device_snmp_router.save()

device_router = Devicedb(name='网关路由器',
                         ip='137.78.5.5',
                         description='QYTANG北京网关路由器',
                         type=Devicetype.objects.get(name='CSR1000v'),
                         snmp_ro_community='qytangro',
                         snmp_rw_community='qytangrw',
                         ssh_username='qytangadmin',
                         ssh_password='Cisc0123',
                         enable_password='Cisc0123')
device_router.save()

gw = Devicedb.objects.get(name='网关路由器')
print(gw)

for x in range(50):
    c = Devicecpu(device=gw, cpu_usage=randint(1, 100))
    c.save()
    sleep(1)

snmp_info = gw.type.devicesnmp.all()

for snmp in snmp_info:
    print(f"SNMP类型:{snmp.snmp_type.name:<20}| OID:{snmp.oid}")

cpu_info = gw.cpu_usage.all()
for cpu in cpu_info:
    print(f"CPU利用率:{cpu.cpu_usage:<5}| 记录时间:{cpu.record_datetime.strftime('%Y-%m-%d %H:%M:%S')}")