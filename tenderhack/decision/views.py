from django.shortcuts import render, redirect
from .models import MainContract
from .forms import MainContractForm

def update_main_contract(request, pk):
    contract = MainContract.objects.get(pk=pk)
    if request.method == 'POST':
        form = MainContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('history', pk=contract.pk)
    else:
        form = MainContractForm(instance=contract)
    return render(request, 'update_contract.html', {'form': form})

def view_history(request, pk):
    contract = MainContract.objects.get(pk=pk)
    history = contract.records_history.all()
    changes = []
    for i in range(len(history)-1):
        diff = history[i].diff_against(history[i+1])
        changes.append(diff)
        print(dir(diff.changes[0]))
    return render(request, 'history.html', {'changes': changes})