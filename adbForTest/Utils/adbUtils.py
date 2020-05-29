#!/usr/bin/env python
#coding=utf-8

import os
import platform
import subprocess
import re

#判断系统类型
system = platform.system()
if system is "Windows":
    find_uitl = "findstr"
else:
    find_uitl = "grep"



