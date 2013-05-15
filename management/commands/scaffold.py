from django.core.management.base import BaseCommand, CommandError
import os


class Command(BaseCommand):
    
    def handle(self, app_name, klass, *args, **options): 
	
	try:
	    top_dir = os.getcwd()
	    app_path = os.path.join(top_dir, app_name)
            os.makedirs(app_path)
	    _attrs = [a.split(':')[0] for a in args if ':' in a]
            _fields = [f.split(':')[1] for f in args if ':' in f]
        except OSError:
            raise CommandError('App already exists!')


