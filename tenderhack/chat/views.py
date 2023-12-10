from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import Chat, Message, FormMessage

@login_required
def chat_view(request, room_id):
    messages = Message.objects.filter(chat__id=room_id).order_by('sent_time')
    form_messages = FormMessage.objects.filter(chat__id=room_id)
    cur_chat = Chat.objects.get(id=room_id)
    
    contract = cur_chat.main_contract
    can_edit = contract.is_being_edited and contract.last_edited_by != request.user
    
    return render(request, 'chat.html', {
        'room_id': room_id, 'messages': messages, 'form_messages': form_messages, 'chat': cur_chat
    } | {'can_edit': can_edit, 'is_being_edited': contract.is_being_edited} | {
        'contract': contract 
    })

@login_required
def contacts_view(request):
    user = request.user

    if user.role == 'performer':
        chats = Chat.objects.filter(performer=user)
    else:
        chats = Chat.objects.filter(customer=user)

    chats = chats.annotate(last_message_time=Max('message__sent_time')).order_by('-last_message_time')
        
    return render(request, 'contacs.html', {'chats': chats})