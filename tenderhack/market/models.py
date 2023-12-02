from django.db import models
from tender_auth.models import TenderUser
from django.core.exceptions import ValidationError

class Proposal(models.Model):
    user = models.ForeignKey(TenderUser, on_delete=models.CASCADE)

    label = models.CharField(
        null=False,
        help_text="Заголовой для вашей услуги",
        max_length=60
    )

    description = models.CharField(
        null=False, 
        help_text="Напишите о своей услуге.",
        max_length=1000
    )

    main_form = models.JSONField()

    def save(self, *args, **kwargs):
        if self.user.role == 'customer':
            raise ValidationError("Customers cannot create proposals.")
        super().save(*args, **kwargs)

