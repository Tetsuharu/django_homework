#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from qyt_device.views.qyt_device_view_show_devices import show_devices
from qyt_device.models import Devicedb


def delete_device(request, device_id):
    try:
        # 获取对应ID的设备
        m = Devicedb.objects.get(id=device_id)
        # 从数据库中删除设备条目
        m.delete()
        return show_devices(request, successmessage="设备删除成功")
    except Devicedb.DoesNotExist:
        return show_devices(request, errormessage="设备未找到!或者已经被删除!")

