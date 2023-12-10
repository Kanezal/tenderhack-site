from django.shortcuts import render, redirect
from .models import MainContract
from .forms import MainContractForm

from chat.models import Chat

def update_main_contract(request, pk):
    contract = MainContract.objects.get(pk=pk)
    chat = Chat.objects.get(main_contract=contract)
    if request.method == 'POST':
        form = MainContractForm(request.POST, instance=contract)
        if form.is_valid():

            if contract.is_being_edited and contract.last_edited_by != request.user:
                contract.last_edited_by = request.user
                contract.records_history.first().delete()
                form.save()

            elif not contract.is_being_edited:
                contract.is_being_edited = True
                contract.last_edited_by = request.user
                form.save()
                
            return redirect('history', pk=contract.pk)
    else:
        form = MainContractForm(instance=contract)
    return render(request, 'update_contract.html', {'form': form, 'chat': chat})


def view_history(request, pk):
    cfg = {}

    contract = MainContract.objects.get(pk=pk)
    chat = Chat.objects.get(main_contract=contract)
    history = contract.records_history.all()
    changes = []
    for i in range(len(history)-1):
        diff = history[i].diff_against(history[i+1])
        changes.append(diff)
    changes.reverse()    
    
    can_edit = contract.is_being_edited and contract.last_edited_by != request.user

    cfg = cfg | {
        'chat': chat, 'can_edit': can_edit,
        'is_being_edited': contract.is_being_edited,
    }

    if cfg['is_being_edited']:
        cfg['current_conflict'] = changes[-1]
        changes = changes[:-1]

    cfg['changes'] = changes

    return render(request, 'history.html', cfg)


def approve_change(request, pk):
    contract = MainContract.objects.get(pk=pk)
    chat = Chat.objects.get(main_contract=contract)
    # If the contract was edited by the other user, approve it
    if contract.last_edited_by != request.user:
        contract.is_being_edited = False
        contract.last_edited_by = None
        contract.save()
        contract.records_history.first().delete()
        # Check if all specified fields are filled
        fields_to_check = ['law', 'procurement_method', 'conclusion_basis', 'number',
                           'contract_subject', 'conclusion_place', 'procurement_id', 
                           'financing_source', 'amount', 'advance', 'customer_details', 'performer_details', 
                           'signer', 'general_info', 'bank_details', 'contact_details_phone', 
                           'contact_details_email']
        for field in fields_to_check:
            if not getattr(contract, field):
                print(f"Field {field} is not filled")
        if all(getattr(contract, field) for field in fields_to_check):
            # Close the chat if all fields are filled
            chat.is_closed = True
            chat.save()
            return redirect('chat', pk=chat.pk)
    return redirect('history', pk=contract.pk)


def reject_change(request, pk):
    contract = MainContract.objects.get(pk=pk)
    # If the contract was edited by the other user, reject it and revert to the previous version
    if contract.last_edited_by != request.user:
        previous_version = contract.records_history.all()[1]
        for field, value in previous_version.instance.__dict__.items():
            setattr(contract, field, value)
        contract.is_being_edited = False
        contract.last_edited_by = None
        contract.save()
        # Delete the latest history record
        contract.records_history.first().delete()
        contract.records_history.first().delete()

    return redirect('history', pk=contract.pk)

def edit_change(request, pk):
    contract = MainContract.objects.get(pk=pk)
    return redirect('history', pk=contract.pk)