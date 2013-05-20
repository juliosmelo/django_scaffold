#Awesome scaffold for DJANGO 1.5+ projects

###Instalation

    pip install django_scaffold

###Usage

    python manager.py scaffold post Post title:string body:text active:boolean

The code above will generate a django app with model, views and urls path.

The example above will create a follow code and files

>post/models.py

    from django.db import models
    from django.core.urlresolvers import reverse


    class Post(models.Models):
        title = models.CharField(max_length=100)
        body = models.TextField()
        active = models.BooleanField()

        def __unicode__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('post_detail_path', kwargs={'pk' : self.pk })

>post/views.py

    from .models import Post
    from django.view.generic.detail import DetailView
    from django.view.generic.list import ListView
    from django.view.generic.edit import CreateView, UpdateView, DeleteView

    class PostDetailView(DetailView):
        model = Post

    class PostCreateView(CreateView):
        model = Post

    class PostUpdateView(UpdateView):
        model = Post

    class PostDeleteView(DeleteView):
        model = Post

    class PostListView(ListView):
        model = Post

>post/urls.py


    from django.conf.url import patterns, url
    from .views import *

    urlspatterns = patterns('',
        url(r'post/(?<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_update_path'),
        url(r'post/(?<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete_path'),
        url(r'post/$', PostListView.as_view(), name='post_index_path'),
        url(r'post/add/$', PostCreateView.as_view(), name='post_create_path'),
        url(r'post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_path'),
    )

>post/forms.py

    from django import forms

    class PostForm(forms.ModelForm):
        class Meta:
            model = Post



###Contribute
1. Fork it!
2. Do things!
3. pull request me!

####Contact

juliocsmelo@gmail.com
