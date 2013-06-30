#Awesome scaffold for DJANGO 1.5+ projects

###Instalation

    pip install django_scaffold

###Usage

    python manager.py scaffold post Post title:string body:text active:boolean

###After

You need add "post" app to INSTALLED_APPS tuple in your settings.py.

The code above will generate a django app with model, views and urls path.

The example above will create the codes and files bellow

>post/models.py

    from django.db import models
    from django.core.urlresolvers import reverse


    class Post(models.Models):
        created_at = models.DateTimeField(auto_add_now=True)
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
    from django.core.urlresolvers import reverse_lazy
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
        success_url = reverse_lazy('post_index_path')

    class PostListView(ListView):
        model = Post

>post/urls.py


    from django.conf.url import patterns, url
    from .views import *

    urlspatterns = patterns('',
        url(r'(?<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_update_path'),
        url(r'(?<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete_path'),
        url(r'^$', PostListView.as_view(), name='post_index_path'),
        url(r'add/$', PostCreateView.as_view(), name='post_create_path'),
        url(r'(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail_path'),
    )

>post/forms.py

    from django import forms
    from .models import Post

    class PostForm(forms.ModelForm):
        class Meta:
            model = Post


>post/templates/post/post_detail.html

    {% load i18n %}
    <p>Created_at: {{ object.created_at }}</p>
    <p>Title: {{ object.title }}</p>
    <p>Body: {{ object.body }}</p>
    <p>Active: {{ object.active }}</p>

>post/templates/post/post_form.html

    {% load i18n %}
    <h2>Post</h2>
    <form action="." method="post">
    {% csrf_token %}
        {{ form.as_table }}
    <input type="submit" value="{% trans "Save" %}"/>
    </form>
>post/templates/post/post_list.html

>post/templates/post/post_confirm_delete.html

    {% load i18n %}
    <p>{% blocktrans with escaped_object=object %}Are you sure you want to delete the {{ object }} "{{ escaped_object }}"? {% endblocktrans %}</p>
    <form action="." method="post">
    {% csrf_token %}
    <input type="submit" value="{% trans "Yes, I'm sure" %}"/>
    </form>
    <a href="{% url 'email_index_path' %}">{% trans "Back" %}</a>


###Contribute
1. Fork it!
2. Do things!
3. pull request!

####Contact
juliocsmelo@gmail.com
