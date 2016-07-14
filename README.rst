django-minimal-abstract-user
============================

By default, Django custom ``User`` model suffers from the following:

* If you derive from ``django.contrib.auth.models.base_user.AbstractBaseUser`` you don't get Django Admin integration, permissions and ``manage.py createsuperuser`` (a real deal breaker for simpler projects!)
* If you derive from ``django.contrib.auth.models.AbstractUser`` you get hard-coded ``username``, ``first_name``, ``last_name`` and ``email`` (what if you don't need to separate first and last name, and don't need usernames at all?)

This library provides a better ``AbstractUser`` class which works around both problems and provides a minimal abstract base ``User`` model that doesn't have any extra fields but supports permissions and Django Admin.


Installation
============

::

        pip install django_minimal_abstract_user


Usage
=====

.. code:: python

	# yourproject/accounts/models.py

	from django_minimal_abstract_user import AbstractUser

	class User(AbstractUser):
		full_name = models.CharField(max_length=60)
		email = models.EmailField(_('email address'), unique=True)
		
		USERNAME_FIELD = 'email'
		REQUIRED_FIELDS = ['full_name']  # Optional


	# yourproject/settings.py
	
	AUTH_USER_MODEL = 'accounts.User'
