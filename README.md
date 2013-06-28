=====
django-singleton-admin
=====

This package provides a way to ensure singleton classes can only have one instance in the
Django admin panel. The package contains:

* admin.py, which defines the SingletonAdmin class, preventing adding if an instance already exists.
* templates/admin/singleton_enabled_base.html, which hides the relevant "add" buttons on the admin.

The admin.py file is taken directly from Mezzanine by Stephen McDonald,
https://bitbucket.org/stephenmcd/mezzanine/src/

The template file is taken from a talk at SyDjango by Stephen McDonald,
http://blog.jupo.org/2012/10/26/sydjango-talk-django-admin-missing-manual/ 


Requirements
--------------

See Mezzanine for more details.


Quick start
-----------

1. Add the app to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = (
            ...
            'django_singleton_admin',
        )

2. In your singleton model's admin.py file, register it with the admin using this class, e.g.::

		from django_singleton_admin.admin import SingletonAdmin

        class GlobalSettingsAdmin(SingletonAdmin):
            pass

        admin.site.register(BSGlobalSettings, GlobalSettingsAdmin)


3. Extend the admin template "admin/base_site.py" using the provided base instead of
   of the usual "admin/base.html", i.e. using:

        {% extends "admin/singleton_enabled_base.html" %}

Note that this template uses the "extrastyle" block, so if you also override that, you
will need to copy the contents of the provided template into your code instead.
(In that case you may not need to add the app to your installed apps either.)

