from django.shortcuts import render, HttpResponseRedirect

from django.http import JsonResponse
from chat.models import Chat, FormMessage

from django.views.decorators.csrf import csrf_exempt
import json

from . import models
from .forms import ProposalForm

def market_view(request):
    proposals = models.Proposal.objects.all()

    context = {
        "proposals": proposals
    }

    if request.method == 'POST':
        form = ProposalForm(request.POST)

        if not form.is_valid():
            context['form'] = form
            return render(request, "market.html", context=context)

        proposal = form.save(commit=False)
        proposal.user = request.user
        proposal.save()
        return HttpResponseRedirect('/market/')
    else:
        form = ProposalForm()
        context['form'] = form

    return render(request, "market.html", context=context)


def detail_view(request, id):
    proposal = models.Proposal.objects.get(id=id)

    context = {
        "proposal": proposal,
        "detail_id": id,
    }

    return render(request, "detail.html", context=context)


@csrf_exempt
def submit_proposal(request, id):
    if request.method == 'POST':
        proposal = models.Proposal.objects.get(id=id)
        form_data = json.loads(request.body)
        chat = Chat.objects.create(legacy=proposal, performer=proposal.user, customer=request.user)
        FormMessage.objects.create(sender=request.user, form=form_data, chat=chat, completed=True)
        return JsonResponse({"status": "success", "chat_id": chat.id})
    else:
        return JsonResponse({"status": "invalid request"})
