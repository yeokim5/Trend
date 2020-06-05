import re
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django import forms
from django.views.generic import CreateView
from django.http import JsonResponse
import json
from fapp.apimongo import doFiles
from collections import Counter

# 요청시 실행될 메서드들

# 1.요청시 방가! 장고 텍스트를 리턴
def rtnBangga(request):
    return HttpResponse("방가? 백주한!")

# 2.문장출력
def doMessage2(request):
    # 검색어 / 컬렉션이름을 받아서 검색하고 몽고디비에 저장
    json_list = doFiles(request.GET.get('txtColname'),request.GET.get('txtColname'),request.GET.get('selClass'),request.GET.get('selClass2'),)
    return JsonResponse(json_list, content_type='application/json', safe=False,json_dumps_params={'ensure_ascii':False})


def doMessage(request):
    return render(request, "fapp/message.html", { "title": "메세지타이틀", "message": "메세지 ㅋㅋ", "content": "메세지 컨텐트입니다. "})

# 3.문장출력
def doDate(request):
    return render(request, "fapp/date.html", { "title": "데이트타이틀", "date": datetime.now(tz=None), "content": "데이트 컨텐트입니다. "})

# 4.문장출력
def doTime(request):
    return render(request, "fapp/date.html", { "title": "Time타이틀", "date": datetime.now(tz=None), "content": "타임 컨텐트입니다. "})

