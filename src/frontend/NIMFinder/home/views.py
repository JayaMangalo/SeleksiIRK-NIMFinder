from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from urllib.parse import urlencode

from .forms import ActionForm
import sys
import os
x = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir))
sys.path.append(x)
from backend import Search as Srch
# insert at 1, 0 is the script path (or '' in REPL)
# x = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir))
# sys.path.append(x)

DISPLAYED_ITEMS_PER_BATCH = 20

currentbatch = 0 
totalfound = 0
datalist = [0,0,0,0]
previousquery = ""

def redirect_params(url, params=None):
     response = redirect(url) #TODO: problem redirect reverse ??
     if params:
          query_string = urlencode(params) 
          response['Location'] += '?' + query_string
     return response

def search_view(request):
     form = ActionForm(request.POST) #TODO: problem form not valid
     if form.is_valid():
          searchquery = form.cleaned_data['ACTION']
          params = {'query': searchquery}
          return redirect_params('home',params)
     return HttpResponseRedirect('')

def SearchRequest(query):
     global previousquery
     previousquery = query

     global datalist
     datalist = Srch.Search(query)
     
     global totalfound
     totalfound = len(datalist)
     
     global currentbatch
     currentbatch = 1
     print(datalist[:5])
                    
def ShowMore(request):
     global currentbatch
     currentbatch+=1
     next = request.POST.get('next', '/')
     return HttpResponseRedirect(next)


def index(request):
     form = ActionForm()

     if 'query' in request.GET:
          query = request.GET.get('query')
          global previousquery
          print("QUERY: ",query)
          print("PREV QUERY: ",previousquery)
          if query != previousquery:
               print("SEARCHED")
               SearchRequest(query)

     global datalist
     global totalfound
     global currentbatch

     displayedmax = min((currentbatch)*DISPLAYED_ITEMS_PER_BATCH,totalfound)

     if displayedmax == totalfound:
          isdisplayedall = True
     else:
          isdisplayedall = False
          
     displayeddata = datalist[:displayedmax]
     template = loader.get_template('home/index.html')
     context = {
          'displayeddata': displayeddata,
          'displayedmax':displayedmax,
          'totalfound':totalfound,
          'isdisplayedall':isdisplayedall,
          'form':form
     }
     return HttpResponse(template.render(context, request))