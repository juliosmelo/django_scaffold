from django.core.management.base import BaseCommand, CommandError
import os
from django_scaffold.core import FIELD_TYPES, PEP8_INDENT, GENERIC_VIEWS, GENERIC_TEMPLATE_NAMES, URLS_PATH

class Command(BaseCommand):

    project_name = os.path.basename(os.getcwd())#get project name

    def handle(self, app_name, klass, *args, **options):

	try:
	    top_dir = os.getcwd()
	    app_path = os.path.join(top_dir, app_name)
            os.makedirs(app_path)
            self.stdout.write('Creating project scaffold...')
            self.create_project_scaffold(app_path, app_name)
            self.create_form(app_path, klass)
            self.create_model(app_path, klass, args)
            self.create_views(app_path, klass)
            self.create_urls(app_path, app_name, klass)
            self.add_appurl_to_urlspy(app_name)
            self.create_adminpy(app_path, klass)
            self.create_list_view(app_path, klass, app_name, args)
            self.stdout.write('Done!')
        except OSError:
            raise CommandError('App already exists!')


    def create_form(self, app_path, klass):
        with open(os.path.join(app_path, 'forms.py'), 'w') as form_file:
            form_file.write('from django import forms\n')
            form_file.write('from .models import {0}\n\n'.format(klass.capitalize()))
            form_file.write('class {0}(forms.ModelForm):\n'.format(klass.capitalize()))
            form_file.write(PEP8_INDENT+'class Meta:\n')
            form_file.write(PEP8_INDENT*2+'model={0}\n'.format(klass.capitalize()))
        form_file.close()
        return

    def create_model(self, app_path, klass, attrs):
        with open(os.path.join(app_path, 'models.py'), 'w') as model_file:
            model_file.write('from django.db import models\n')
            model_file.write('from django.core.urlresolvers import reverse\n\n')
            model_file.write('class {0}(models.Model):\n'.format(klass.capitalize()))
            model_file.write(PEP8_INDENT+'created_at=models.DateTimeField(auto_now_add=True)\n')
            for attr in attrs:
                field_name, field_type = attr.split(':')[0], attr.split(':')[1]
                model_file.write(PEP8_INDENT+'{0}={1}\n'.format(field_name, self.get_field_type(field_type)))
            model_file.write('\n')
            model_file.write(PEP8_INDENT+'def __unicode__(self):\n')
            model_file.write(PEP8_INDENT*2+'return self.{0}\n\n'.format(attrs[0].split(':')[0].lower()))
            model_file.write(PEP8_INDENT+'def get_absolute_url(self):\n')
            model_file.write(PEP8_INDENT*2+"return reverse('%s_detail_path', kwargs={'pk': self.pk})\n\n"%(klass.lower()))
        model_file.close()
        return

    def create_project_scaffold(self, app_path, app_name):
        folders=['static/{0}/css/'.format(app_name),'static/{0}/javascript'.format(app_name.lower()),
                 'static/{0}/images'.format(app_name), 'templates/{0}'.format(app_name.lower())]
        for folde in folders:
            os.makedirs(os.path.join(app_path, folde))
        with open(os.path.join(app_path, '__init__.py'), 'w') as f:
            f.close()
        return

    def create_views(self, app_path, klass):
        with open(os.path.join(app_path, 'views.py'), 'w') as view_file:
            view_file.write('from .models import {0}\n'.format(klass.capitalize()))
            view_file.write('from django.views.generic import DetailView, ListView\n')
            view_file.write('from django.views.generic.edit import CreateView, UpdateView, DeleteView\n\n')
            for view in GENERIC_VIEWS:
                view_file.write('class {0}{1}({2}):\n'.format(klass.capitalize(), view, view))
                view_file.write(PEP8_INDENT+'model = {0}\n\n'.format(klass.capitalize()))
        return


    def create_adminpy(sefl, app_path, klass):
        with open(os.path.join(app_path, 'admin.py'), 'w') as admin_file:
            admin_file.write('from django.contrib import admin\n')
            admin_file.write('from .models import {0}\n\n'.format(klass))
            admin_file.write('admin.site.register({0})\n'.format(klass))
        admin_file.close()
        return



    def create_urls(self, app_path, app_name, klass):
        with open(os.path.join(app_path, 'urls.py'), 'w') as urls_file:
            urls_file.write('from django.conf.urls import patterns, url\n')
            generic_views_list = [k for k, v in URLS_PATH.items()]
            generic_views = map(lambda u:'{0}{1}'.format(klass.capitalize(), u), generic_views_list)
            urls_file.write('from .views import {0}\n\n'.format((', ').join(generic_views)))
            urls_file.write("urlpatterns = patterns('', \n")
            for k,v in URLS_PATH.items():
                urls_file.write(PEP8_INDENT+"url(r'{app}/{url}', {klass}{gview}.as_view(), name='{app}_{url_name}'),\n".format(app=app_name, klass=klass.capitalize(), gview=k, url=v['url'], url_name=v['name']))
            urls_file.write(')\n')
        urls_file.close()
        return

    def add_appurl_to_urlspy(self, app_name):
        #get project urls.py
        with open(os.path.join(os.getcwd(), self.project_name, 'urls.py'), 'a') as urlspy_file:
            urlspy_file.write("urlpatterns += patterns('',\n{pep8}url(r'^{app}/', include('{app}.urls'))\n)".format(app=app_name, pep8=PEP8_INDENT))
        urlspy_file.close()
        return

    def get_field_type(self, ftype):
        return FIELD_TYPES.get(ftype)

    #views
    def create_list_view(self, app_path, klass, app_name, args):
        template_path = os.path.join(app_path, 'templates', app_name)
        template_name = '{0}_list.html'.format(klass)
        with open(os.path.join(template_path, template_name.lower()), 'w' ) as tpl_file:
            tpl_file.write('{% load i18n %}\n')
            tpl_file.write('<h2>{klass}</h2>\n'.format(klass=klass))
            tpl_file.write('\t<ul syle="list-style:inline;">\n')
            tpl_file.write('\t\t{% for object in object_list %}\n')
            _attrs = map(lambda attr: attr.split(':')[0], args)
            for attr in _attrs:
                tpl_file.write('\t\t\t<li>{{ object.'+attr+' }}</li>\n')
            tpl_file.write('\t\t{% endfor %}\n')
            tpl_file.write('\t</ul>\n')
            tpl_file.write("<a href={% url '{0}_create_path' %}>{% trans 'Save' %}</a>".format(app_name))
        tpl_file.close()
        return
