from django.shortcuts import render
import re

# Create your views here.

from django.views.generic import TemplateView
from .forms import InputForm


class CookieView(TemplateView):
  template_name = 'home.html'

  def get(self, request, *args, **kwargs):
    return render(request,self.template_name, {'form': InputForm })


  def post(self, request, *args, **kwargs):
    abc=[]
    bcd={}
    input = request.POST['input']
    print input,"\n\n\n\n\n#######################\n\n\n\n\n"
    f=input.split(';')
    data=[]
    for i in f :
      if i:
        data.append(i)
    print data
    for i in data:
      print i,"4$$$$$$$"
      searchObj = re.findall( r'^(.*?)=',i, re.M|re.I)
      a =  searchObj[0]
      b = i[len(a)+1:]
      # obj= "'"+a+"':'"+b+"'"
      # obj = a+ ":" +b
      # abc.append(obj)
      bcd[str(a)]=str(b);

    # bcd = [str(i).strip() for i in bcd]
    # for i in abc:
    #   print i,"abc"
    #   bcd.update(i)

    return render(request,self.template_name, {'form': InputForm({'input':input, 'output': bcd}) })

