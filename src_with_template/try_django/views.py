# Changing what a page looks like you start with the view. Dont do HTML
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.http import FileResponse, Http404

# These are the defined views
# Going to any page requires a request and returns a response
def home_page(request):
    my_title = "Welcome to Saif's Site"
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1,2,3,4,5]}
    else:
        context = {"title": my_title, "authentication_error": "Please Login"}
    return render(request, "home.html", context)

def about_page(request):
    return render(request,"about.html",  {"title": "About Us"})

def contact_page(request):
    return render(request,"about.html",  {"title": " Us"})

def pdf_page(request):
    context = {"title": "PDF Page"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)

    return HttpResponse(template_obj.render(context))
