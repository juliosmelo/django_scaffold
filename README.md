#Awesome scaffold for DJANGO 1.5+ projects
###Instalation
    pip install django_scaffold

###Usage
>python manager.py scaffold post Post title:string body:text
active:boolean

The code above will generate a django app with model, views and urls path.

The example above will create a follow model

    class Post(models.Models):
        title = models.CharField(max_length=100)
        body = models.BooleanField()
        def __unicode__(self):
            return self.title`

###Contribute

