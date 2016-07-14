from django.contrib.auth.models import AbstractUser as AbstractUserWithJunk
from django_abstract_utils import without


AbstractUser = without(AbstractUserWithJunk, 'username', 'first_name', 'last_name', 'email')
AbstractUser.REQUIRED_FIELDS = []
