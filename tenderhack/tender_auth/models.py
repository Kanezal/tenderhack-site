from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

USER_ROLES = (
    ('performer', 'Исполнитель'),
    ('customer', 'Заказчик'),
)

class TenderUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class TenderUser(AbstractBaseUser):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES)

    objects = TenderUserManager()
    USERNAME_FIELD='email'

