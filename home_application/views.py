# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def helloworld(request):
    """
    helloworld
    """
    data = [
        {
            "use": "20%",
            "ip": "10.0.1.14",
            "filesystem": "/dev/vda1",
            "mounted": "/",
            "createtime": "2018-07-11 22:31:01",
            "size": "50G"
        },
        {
            "use": "0%",
            "ip": "10.0.1.14",
            "filesystem": "devtmpfs",
            "mounted": "/dev",
            "createtime": "2018-07-11 22:31:01",
            "size": "7.8G"
        }
    ]
    return render_json({'result':False, 'data':data, 'message':u'token不合法'})
    # return render_mako_context(request, '/home_application/helloworld.html')
