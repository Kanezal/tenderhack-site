from django.db import models
from tender_auth.models import TenderUser


class Chat(models.Model):
    performer = models.ForeignKey(TenderUser, related_name='performer', on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(TenderUser, related_name='customer', on_delete=models.CASCADE, null=True)

    main_form = models.ForeignKey('decision.MainContract', on_delete=models.CASCADE, null=True)
    
    creation_date = models.DateTimeField(auto_now_add = True)

    is_closed = models.BooleanField(default = False)
    is_failed = models.BooleanField(default = False)

    status = models.CharField(max_length = 255, default = 'active')


class Message(models.Model):
    sender = models.ForeignKey(TenderUser, on_delete = models.CASCADE, null = True, related_name = 'message_sender')
    text = models.TextField()
    
    sent_time = models.DateTimeField(auto_now_add=True)

    chat = models.ForeignKey(Chat, on_delete = models.CASCADE, null=True)

    is_read = models.BooleanField(default = False)


class FormMessage(models.Model):
    sender = models.ForeignKey(TenderUser, on_delete = models.CASCADE, null = True, related_name = 'form_message_sender')
    
    form = models.JSONField()

    chat = models.ForeignKey(Chat, on_delete = models.CASCADE, null=True)

    completed = models.BooleanField(default = False)