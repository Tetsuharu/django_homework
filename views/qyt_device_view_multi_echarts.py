#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.shortcuts import render
from qyt_device.models import Devicedb
from qyt_device.views.qyt_device_view_make_echarts_data import data_from_db
import json
import random


def multi_echarts(request):
    all_data = data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar'], last_hours=1.5)
    all_data = data_from_db(Devicedb.objects.filter(name='R1'), ['#00BFFF'], ['bar'], last_hours=1.5)
    # 饼状图2数据
    pie2_label = '协议分布'
    pie2_protocol = ['HTTP', 'Telnet', 'SSH', 'ICMP']
    pie2_data = [{'value': random.randint(20, 100), 'name': p} for p in pie2_protocol]
    return render(request, 'qyt_device_multi_echarts.html', {
                                                             'chart2_label': 'CPU利用率',
                                                             # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                                             # 图标的列表
                                                             'chart2_legends': json.dumps(all_data[0]),
                                                             # X轴时间的列表
                                                             'chart2_time': json.dumps(all_data[1]),
                                                             # 多个设备(多线)的数据
                                                             'chart2_data': json.dumps(all_data[2]),
                                                             # 饼状图2 Django数据
                                                             # 饼状图名称
                                                             'pie2_label': json.dumps(pie2_label),
                                                             # 协议列表
                                                             'pie2_protocol': json.dumps(pie2_protocol),
                                                             # 协议数据
                                                             'pie2_data': json.dumps(pie2_data),
                                                             })
