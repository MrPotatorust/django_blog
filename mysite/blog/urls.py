from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("",views.main_page, name="main_page"),
    path("blogs/",views.BlogListView.as_view(), name="blog_list"),
    path("blog_post/<int:pk>/", views.BlogpostView.as_view(), name="blogpost"),
    path("newest_blog/", views.newest_blog, name="newest_blog"),
]