#!/usr/bin/python
# -*- coding:utf-8 -*-

import winroute.winroute as winroute
import os

#实例
route=winroute.WinRoute()

#输出当前路由表（IPv4）
# route.printroute()

#添加一个路由，给出：目标IP，子网掩码，网关(即下一跳IP，不给出与默认路由的相同)，Metric值（不给出则与默认路由的相同），接口（不给出则与默认路由的相同）
# route.CreateIpForwardEntry("203.205.128.0","255.255.128.0")
route.DeleteIpForwardEntry("118.112.11.0","255.255.255.0")
# exit(233)
with open(os.path.split(os.path.realpath(__file__))[0]+'/add.txt') as file:
    for line in file:
        arr = line.split(" ")
        print(arr[0])
        try:
            route.DeleteIpForwardEntry(arr[0],arr[1])
        except:
            pass
file.close()