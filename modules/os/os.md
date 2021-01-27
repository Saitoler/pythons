# 此模块提供一些使用操作系统相关功能的函数
+ 读写文件：          open()
+ 操作路径：          os.path 模块
+ 创建临时文件和目录： tempfile 模块
+ 高级文件目录处理：   shutil   模块

> 所有接受路径或文件名的函数，都同时支持字符串和字符串对象，并在返回路径或文件名时，使用相应类型的对象作为结果。

## os.name() - 返回当前平台信息
> 返回值目前仅有三个：  
+ posix - Linux(Mac)
+ nt    - Windows
+ java  - Java 虚拟机
> 在 sys.platform 中可以获取到相对更详细的信息：
	sys.platform:
	+ Mac OS X:  	  darwin
	+ Linux:          linux
	+ Windows/cygwin: cygwin

## os.path 模块
> 常见的文件操作：
+ os.path.abspath(path)
	> 返回 path 的绝对路径(标准化的)，可接受一个 path-like 对象，参见 demo1
+ os.path.basename(path) 
	> 返回路径 path 的基本名称，即返回当前所在最近目录的目录名称，参见 demo2
+ os.path.dirname(path)
	> 返回 path 的父目录的绝对路径，参见 demo3
+ os.path.exists(path)
	> 如果 path 是已存在的路径，返回 **True**；对于失效的符号链接，返回 **False** 参见 demo4
+ os.path.getatime(path)
	> + 返回 path 的最后访问时间-返回值是一个浮点数，为纪元秒数。  
	> + 纪元秒数可以通过 time.localtime(t) 转换为一个 struct time 对象  
	> + struct time 对象再通过 time.strftime(format, t) 格式化为符合人类可读形式的时间  
	
	> 参见 demo5

