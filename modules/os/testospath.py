# -*- coding: utf-8 -*-

import os
import time
import os.path

# Demo1
# os.path.abspath(path) - 返回 path 的绝对路径（标准化的）
print(os.path.abspath(".")) # /Users/saitoler/Documents/gitdir/pythons/libs -打印当前路径的绝对路径出来

# Demo2
# os.path.basename(path) - 返回 path 的基本名称,即返回当前所在的目录的目录名称
print(os.path.basename(os.path.abspath("."))) # libs
print(os.path.basename("/local/user")) # user

# Demo3
# os.path.dirname(path) 返回 path 的父目录的绝对路径：
print(os.path.dirname(os.path.abspath("."))) # /Users/saitoler/Documents/gitdir/pythons

# Demo4
# os.path.exists(path) - 若 path 存在，则返回 True，否则返回 False；失效符号链接也返回 False
print(os.path.exists("/usr/local")) # True
print(os.path.exists("/111/222/333")) # False

# Demo5
accessTime = os.path.getatime("./os/os.md")
print(time.strftime("%H:%M:%S",time.localtime(accessTime)))