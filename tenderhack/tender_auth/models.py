from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = (
    ('performer', 'Исполнитель'),
    ('customer', 'Заказчик'),
)

class TenderUser(AbstractUser):
    role = models.CharField(max_length=20, choices=USER_ROLES)