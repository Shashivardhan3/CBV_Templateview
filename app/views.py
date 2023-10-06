

from typing import Any
from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView


class Template(TemplateView):
    template_name='templateview.html'


class insert_by_template(TemplateView):
     template_name='insert_by_template.html'

     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
          ECDO= super().get_context_data(**kwargs) #empty context data object 
          ECDO['SFO']=StudentForm
          return ECDO
     def post(self,request):
          SFDO=StudentForm(request.POST)
          if SFDO.is_valid():
               SFDO.save()
          return HttpResponse('data is inserted')