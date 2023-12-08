from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import Chat, Message, FormMessage

def chat_view(request, room_id):
    messages = Message.objects.filter(chat__id=room_id).order_by('sent_time')
    form_messages = FormMessage.objects.filter(chat__id=room_id)
    
    return render(request, 'chat.html', {'room_id': room_id, 'messages': messages, 'form_messages': form_messages})

@login_required
def contacts_view(request):
    user = request.user

    if user.role == 'performer':
        chats = Chat.objects.filter(performer=user)
    else:
        chats = Chat.objects.filter(customer=user)
    print(chats)
    chats = chats.annotate(last_message_time=Max('message__sent_time')).order_by('-last_message_time')
    
    for chat in chats:
        chat.unread_messages = Message.objects.filter(chat=chat, is_read=False).count()
    
    return render(request, 'contacs.html', {'chats': chats})