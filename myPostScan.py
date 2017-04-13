# -*- coding: utf-8 -*-
# __author__:scriptboy
#__如果有什么问题请联系作者：437082581@qq.com
#__感谢@dj__:运用python成为顶级黑客
import socket
import argparse
import threading
arg_=argparse.ArgumentParser()
arg_.add_argument('-H',help=u'-H代表是主机',dest='host') #2.7版本以后出现的模块，参数模块
arg_.add_argument('-P',help=u'-P代表是端口',dest='port')
yu=arg_.parse_args()
# print yu.host,yu.port
# print type(yu.host)
host=yu.host
port=yu.port
if(host==None) or (port==None):#如果是空参数，直接退出
    exit(0)
else:
    print host,port
scrlock=threading.Semaphore(value=1)
def connect_tg(host,port):
    try:
        socket_scan=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        p_tuple=(host,port)#把主机和端口放在一个元组中
        socket_scan.connect(p_tuple)#连接
        socket_scan.send(u'hello,server\r\n')
        result=socket_scan.recv(1024)
        scrlock.acquire()
        print result
        print u'%d端口是开放的\r' % (port)
    except:
        scrlock.acquire()
        print u'{}端口是关闭的\r'.format(port)
    finally:
        scrlock.release()
        socket_scan.close()
def portScan(tghost,taport):
    try:
        tgIP=socket.gethostbyname(tghost)
    except:
        print u'无法解析地址%s'%(tghost)
        return
    socket.setdefaulttimeout(1)
    taport=taport.split(',')#他会把输入的当成一个字符串处理，在这个把他转换成一个列表，最后迭代
    for tgp in taport:
        #print u'正在扫描目标端口'+str(tgp)
        #connect_tg(tghost, tgp)
        t=threading.Thread(target=connect_tg,args=(tghost,int(tgp)))
        t.start()
#portScan('www.scjfund.com',[80,443,3389,1433,23,445])
portScan(host,port)