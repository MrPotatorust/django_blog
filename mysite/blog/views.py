from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Blogpost
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.


def main_page(request):
    return render(request, "blog/index.html", {"posts": Blogpost.objects.all()[:5]})


def newest_blog(request):
    return redirect(reverse("blog:blogpost", kwargs={"pk": 1}))


class BlogListView(generic.ListView):
    template_name = "blog/blog_list.html"
    context_object_name = "blog_post_list"


    def get_queryset(self):
        return Blogpost.objects.order_by("pub_date")
    

class BlogpostView(generic.DetailView):
    model = Blogpost
    template_name = "blog/blogpost.html"

    def get_queryset(self):
        return Blogpost.objects.all()