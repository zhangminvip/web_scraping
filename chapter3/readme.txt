
downloader.py

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
or
http://blog.sina.com.cn/s/blog_3fe961ae0100nuzg.html
,具体可以看这个链接，也可以进去看Request的源代码，好了，我们已经获取到了一个request对象，下面，我们需要一个opener,如果类本身的opener是None，就创建一个opener, 接下来，判断proxy是否是None,不是的话我们就需要进行一些设置
http://wiki.jikexueyuan.com/project/python-crawler/opener-and-handler.html
可以看看这篇文章，注意这个response对象，他的方法，read() 和属性.code , 如果捕获到异常，先确保html问空字符串，判断如果异常有code属性，获取code,判断如果是服务器的异常，执行下载函数，返回result.


disk_cache.py

先看一下前面的导包部分，shutil 和os 和文件的操作有关，zlib是数据压缩的，timedelta对象代表两个时间之间的时间差，然后一个一样捕捉，这里要解释一下cPickle和pickle

敲黑板！

pickle模块使用的数据格式是python专用的，并且不同版本不向后兼容，同时也不能被其他语言说识别。要和其他语言交互，可以使用内置的json包
  使用pickle模块你可以把Python对象直接保存到文件，而不需要把他们转化为字符串，也不用底层的文件访问操作把它们写入到一个二进制文件里。pickle模块会创建一个python语言专用的二进制格式，你基本上不用考虑任何文件细节，它会帮你干净利落地完成读写独享操作，唯一需要的只是一个合法的文件句柄。
    pickle模块中的两个主要函数是dump()和load()。dump()函数接受一个文件句柄和一个数据对象作为参数，把数据对象以特定的格式保存到给定的文件中。当我们使用load()函数从文件中取出已保存的对象时，pickle知道如何恢复这些对象到它们本来的格式。
    dumps()函数执行和dump()函数相同的序列化。取代接受流对象并将序列化后的数据保存到磁盘文件，这个函数简单的返回序列化的数据。
    loads()函数执行和load()函数一样的反序列化。取代接受一个流对象并去文件读取序列化后的数据，它接受包含序列化后的数据的str对象, 直接返回的对象。
    cPickle是pickle得一个更快得C语言编译版本。

解释完了。



而对于 cache 类， 我们可以通过调用 result = cache [url ］ 从 cache
中加载数据， 并通过 cache [url ] = result 向 cache 中保存结果。 大家
应该很熟悉这种便捷的接 口 写法， 因为这也是 ηthon 内 建字典数据类型的使
用方式 。 为 了支持该接 口 ， 我们 的 cache 类需要定义__getitem__ (  ) 和
__setitem__( )这两个特殊的类方法.










