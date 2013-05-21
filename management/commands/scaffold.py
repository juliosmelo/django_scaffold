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
            self.create_project_scaffold(app_path, app_name)
            self.create_form(app_path, klass)
            self.create_model(app_path, klass, args)
            self.create_views(app_path, klass)
            self.create_urls(app_path, app_name, klass)
            self.add_appurl_to_urlspy(app_name)
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
        self.stdout.write('Creating project folders')
        folders=['static/{0}/css/'.format(app_name),'static/{0}/javascript'.format(app_name.lower()),
                 'static/{0}/images'.format(app_name), 'templates/{0}'.format(app_name.lower())]
        for folde in folders:
            os.makedirs(os.path.join(app_path, folde))
        return self.stdout.write('Done!')

    def create_views(self, app_path, klass):
        with open(os.path.join(app_path, 'views.py'), 'w') as view_file:
            view_file.write('from .models import {0}\n'.format(klass.capitalize()))
            view_file.write('from django.views.generic import DetailView, ListView\n')
            view_file.write('from django.views.generic.edit import CreateView, UpdateView, DeleteView\n\n')
            for view in GENERIC_VIEWS:
                view_file.write('class {0}{1}({2}):\n'.format(klass.capitalize(), view, view))
                view_file.write(PEP8_INDENT+'model = {0}\n\n'.format(klass.capitalize()))
        return

    def create_generic_template(self, app_path, app_name, klass):
        templates_path = os.path.join(app_path, templates, app_name)
        for template in GENERIC_TEMPLATE_NAMES:
            with open() as template_file:
                pass
        return

    def create_urls(self, app_path, app_name, klass):
        with open(os.path.join(app_path, 'urls.py'), 'w') as urls_file:
            urls_file.write('from django.conf.urls import patterns, url\n')
            generic_views_list = [k for k, v in URLS_PATH.items()]
            generic_views = map(lambda u:'{0}{1}'.format(klass.capitalize(), u), generic_views_list)
            urls_file.write('from .views import {0}\n\n'.format((',').join(generic_views)))
            urls_file.write("urlpatterns = patterns('', \n")
            for k,v in URLS_PATH.items():
                urls_file.write(PEP8_INDENT+"url(r'{app}/{url}', {klass}{gview}.as_view(), name='{app}_{url_name}'),\n".format(app=app_name, klass=klass.capitalize(), gview=k, url=v['url'], url_name=v['name']))
            urls_file.write(')\n')
        urls_file.close()
        return

    def add_appurl_to_urlspy(self, app_name):
        #get project urls.py
        with open(os.path.join(os.getcwd(), self.project_name, 'urls.py'), 'a') as urlspy_file:
            urlspy_file.write("urlpatterns += patterns(url(r'{app}', include('{project}.{app}.urls')))\n".format(project=self.project_name,app=app_name))
        urlspy_file.close()
        return

    def get_field_type(self, ftype):
        return FIELD_TYPES.get(ftype)
