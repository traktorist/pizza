from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson as json
from django.utils.decorators import decorator_from_middleware
from django.middleware.gzip import GZipMiddleware
from django.views.decorators.csrf import csrf_exempt
from orderpizza.models import UnitOrder
import time

@decorator_from_middleware(GZipMiddleware)
@csrf_exempt
def times(request):
    now = time.ctime(time.time())
    jsonDict = {'date': now} 
#    if request.is_ajax():
#        print request.raw_post_data        
    return render_to_response('pizza.html', jsonDict)
