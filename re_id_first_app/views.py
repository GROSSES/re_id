from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import os
from django.views.decorators.http import require_http_methods
from datetime import datetime
from django.template import Template,Context
from . import rank


def img_proc(request):
    datalist = []
    if request.method == 'GET':
        img_dir = request.GET.get("img_dir", None)
        print(img_dir)
        time = datetime.now()
        if img_dir is not None:
            rank.rank_save(img_dir)
            with open('matching_info.txt', "r") as f:
                with open('img_info.txt','a+') as f2:
                    f2.write("{}--{}--\n".format(img_dir, time.strftime("%y-%m-%d %H:%M:%S")))
                cnt = 0
                for line in f:
                    cnt = cnt + 1
                    d={"index": cnt,
                       "dir": line
                    }
                    datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "re_id.html", {"data": datalist})


#


