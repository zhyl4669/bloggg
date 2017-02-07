# Create your views here.
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from MyBlog.models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def showStudents(request):
    list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
    return render_to_response('student.html',{'students': list})