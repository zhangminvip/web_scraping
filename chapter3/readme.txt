这里有两个类，一个Downloader,一个Throttle,
Downloader 有一个初始化函数，（也就是java的构造器啦），一个回调函数，一个功能函数（download）

先看初始化函数吧，第一个参数永远是self, 紧接着是延迟时间、用户代理、代理服务器、尝试次数、超时、opener 来自 urllib2.build_opener()这个方法，cache就是缓存啦~

初始化第一件事情，设置全局socket的默认超时，下面一路的定义，创建变量，用到了init函数的所有参数。


下面是定义一个回调函数，

result = None  这样就符合此方法内第二个if的条件啦~

第一个if判断cache是否为None,  cache 是什么？cache是一个包含字典的字典，它包含的字典就是result ， result有两个key,一个是网页的html，一个是服务器状态码code, 
当前是一个try except else 语句，异常处理常用手段，else的条件是没发生异常，try用来获取result，如果缓存中没有这个网页的result,就会发生keyerror,pass是个空语句，什么也不做，用来占位，如果从缓存中获取到了result，就不会触发keyerror异常，就会执行else语句，当发现我们获取到的result中的状态码是服务器错误并且(and)我们预设的尝试次数大于零，就把result重置为None, 这样，就可以顺利执行下面的下载了。


如果一番周折之后，result还是None，都可以下载了，毕竟cache中没有嘛，或者cache中有的也是错的，我们都需要重新下载，先用throttle（节流阀）的wait方法来检查一个这个url上次访问的时间是否满足了延迟，如果满足了，则不需要sleep,如果proxies不是空的情况下在proxies中随机选取一个代理服务器，
否则proxy乖乖等于None,headers中的user-agent用我们预设的啦，然后我们调用download函数去下载一个结果，传入所以该有的参数，已经默认的参数，比如data，可以不用传，但是当然也可以传，去改变默认，获取到result后，判断一下cache是否存在（我没有测试，但是应该如果cache不存在，你去访问的话，会报错的，），返回的是html。

下面我来解释一个download函数，接受四个参数，url , header(里面key是user-agent) , proxy ,  num_retries,  下面urllib2.Request函数的传参用到了
or(http://blog.sina.com.cn/s/blog_3fe961ae0100nuzg.html),具体可以看这个链接，也可以进去看Request的源代码，好了，我们已经获取到了一个request对象，下面，我们需要一个opener,如果类本身的opener是None，就创建一个opener, 接下来，判断proxy是否是None,不是的话我们就需要进行一些设置（http://wiki.jikexueyuan.com/project/python-crawler/opener-and-handler.html）可以看看这篇文章，注意这个response对象，他的方法，read() 和属性.code , 如果捕获到异常，先确保html问空字符串，判断如果异常有code属性，获取code,判断如果是服务器的异常，执行下载函数，返回result.










