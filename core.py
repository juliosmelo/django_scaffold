PEP8_INDENT = ' '*4

FIELD_TYPES = {'string': 'models.CharField(max_length=100)',
               'text': 'models.TextField()',
               'integer': 'models.IntegerField()',
               'file': 'models.FileField()',
               'big_integer':'models.BigIntegerField()',
               'small_integer':'models.SmallIntegerField()',
               'time': 'models.TimeField()',
               'datetime': 'models.DateTimeField()',
               'date': 'models.DateField()',
               'slug': 'models.SlugField()',
               'url': 'models.URLField()',
               'ip': 'models.IPAddressFiedl()',
               'image' : 'models.ImageField()',
               'boolean': 'models.BooleanField()',
               'comma_integer': 'models.CommaSeparatedIntegerField()',
               'decimal' : 'models.DecimalField()',
               'float': 'models.FloatField()',
               'null_boolean' : 'models.NullBooleanField()',
               'positive_integer' :'models.PositiveIntegerField()',
               'positive_small_i':'models.PositiveSmallIntegerField()',
               'file_path': 'models.FilePathField()',
               'generic_ip' :'models.GenericIPAddressField()',
}

GENERIC_VIEWS = ['DetailView', 'CreateView', 'UpdateView', 'DeleteView', 'ListView']

GENERIC_TEMPLATE_NAMES = ['_create_form.html', '_update_form.html', '_confirm_delete.html', '_detail.html', '_list.html']

URLS_PATH = {'DetailView': {'url':'(?P<pk>\d+)/$', 'name':'detail_path'},
             'CreateView': {'url':'add/$', 'name': 'create_path'},
             'UpdateView': {'url':'(?<pk>\d+)/edit/$', 'name': 'update_path'},
             'DeleteView': {'url':'(?<pk>\d+)/delete/$','name':'delete_path'},
             'ListView' :  {'url' : '$', 'name': 'index_path'}
}

