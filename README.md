#Awesome scaffold for DJANGO 1.5+ projects

###Instalation

    pip install django_scaffold

###Usage
>python manager.py scaffold post Post title:string body:text
active:boolean

The code above will generate a django app with model, views and urls path.

The example above will create a follow model

    from django.db import models
    class Post(models.Models):
        title = models.CharField(max_length=100)
        body = models.BooleanField()
        def __unicode__(self):
            return self.title`

View..

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

###Contribute

