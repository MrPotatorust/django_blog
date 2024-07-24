from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Blogpost

# Create your views here.


def main_page(request):
    return render(request, "blog/index.html")



class BlogListView(generic.ListView):
    template_name = "blog/blog_list.html"
    context_object_name = "BlogPost_list"


    def get_queryset(self):
        return Blogpost.objects.all()
    

class BlogpostView(generic.DetailView):
    model = Blogpost
    template_name = "blog/blogpost.html"

    def get_queryset(self):
        return Blogpost.objects.all()