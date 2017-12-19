这里有两个类，一个Downloader,一个Throttle,
Downloader 有一个初始化函数，（也就是java的构造器啦），一个回调函数，一个功能函数（download）

先看初始化函数吧，第一个参数永远是self, 紧接着是延迟时间、用户代理、代理服务器、尝试次数、超时、opener 来自 urllib2.build_opener()这个方法，cache就是缓存啦~

初始化第一件事情，设置全局socket的默认超时，下面一路的定义，创建变量，用到了init函数的所有参数。


下面是定义一个回调函数，

result = None  这样就符合此方法内第二个if的条件啦~

第一个if判断cache是否为None,  cache 是什么？cache是一个包含字典的字典，它包含的字典就是result ， result有两个key,一个是网页的html，一个是服务器状态码code, 
当前是一个try except else 语句，异常处理常用手段，else的条件是没发生异常，try用来获取result，如果缓存中没有这个网页的result,就会发生keyerror,






