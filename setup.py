import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-singleton-admin',
    version = '0.0.3',
    packages = find_packages(),   
    include_package_data = True,
    license = 'BSD', 
    description = """This package provides a way to ensure singleton classes can 
                     only have one instance in the Django admin panel.
                     It is taken from Mezzanine by Stephen McDonald.""",
    long_description = README,
    keywords = "globals singleton",
    url = 'https://github.com/RacingTadpole/django-singleton-admin',
    author = 'Arthur Street',
    author_email = 'arthur@racingtadpole.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe = False,
    install_requires = [
        'django >= 1.4',
    ],
)
