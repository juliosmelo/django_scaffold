from distutils.core import setup

setup(
    name="django_scaffold",
    version=__import__("django_scaffold").__version__,
    description="Scaffold creator for Django 1.5+ projects",
    long_description=open("docs/usage.txt").read(),
    author="Julio Siveira Melo",
    author_email="juliocsmelo@gmail.com",
    url="https://github.com/juliosmelo/django_scaffold/",
    packages=[
        "django_scaffold",
        "django_scaffold.management",
        "django_scaffold.management.commands",
    ],
    package_dir={"mailer": "mailer"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
