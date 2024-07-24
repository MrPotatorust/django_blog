from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Blogpost

# Create your views here.


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "blog_post_list"


    def get_queryset(self):
        return Blogpost.objects.all()