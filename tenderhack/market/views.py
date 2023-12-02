from django.shortcuts import render, HttpResponseRedirect

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

# TODO: дописать это и детали.html
def detail_view(request, id):
    proposal = models.Proposal.objects.get(id=id)

    context = {
        "proposal": proposal
    }

    return render(request, "detail.html", context=context)