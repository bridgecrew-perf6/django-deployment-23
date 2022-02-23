from difflib import context_diff
from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'Hello World!','number':100}
    return render(request,'template_app/index.html',context_dict)

def other(request):
    return render(request,'template_app/other.html')

def relative(request):
    return render(request,'template_app/relative_url_template.html')

     