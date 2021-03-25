# encoding: utf-8
'''
@author: leon
@project: Message
@created: 2018/10/23 18:22
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named other_rest.py in Message
'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from strategy.models import *
from strategy.serializers import *


# Create your views here.
@csrf_exempt
def snippet_list(request):
    """
    列出所有已经存在的snippet或者创建一个新的snippet
    """
    if request.method == 'GET':
        snippets = Receptor.objects.all()
        serializer = ReceptorSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReceptorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    检索查看、更新或者删除一个代码段
    """
    try:
        snippet = Receptor.objects.get(pk=pk)
    except Receptor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReceptorSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReceptorSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)