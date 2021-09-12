
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models 
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     mobile = models.BigIntegerField(default=0)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()


#     def __str__(self):
#         return self.email




class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    age = models.IntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __Str__(self):
        return self.email






























