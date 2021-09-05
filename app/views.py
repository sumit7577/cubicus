from django.shortcuts import render,HttpResponse
from django.template import loader
from django import template
# Create your views here.
def index(request):
    context = {}
    context["segment"] = "index"
    html = loader.get_template("index.html")
    return HttpResponse(html.render(context,request))


def pages(request):
    context = {}
    try:
        load_template = request.path.split("/")[-1]
        print(load_template)
        context["segment"] = load_template
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context,html_template))
    except:
        return HttpResponse("Page Not Found")