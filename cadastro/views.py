from django.shortcuts import render, redirect, get_object_or_404
from .models import CadProd
from .forms import CadForm
from django.contrib.auth.decorators import login_required



@login_required()
def prod_list(request):
    produtos = CadProd.objects.all()
    return render(request, 'prod_list.html', {'produtos': produtos})



@login_required()
def new_prod(request):
    form = CadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('prod_list')

    return render(request, 'form_prod.html', {'form': form})



@login_required()
def prod_up(request, id):
    person = get_object_or_404(CadProd, pk=id)
    form = CadForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()

        return redirect('prod_list')

    return render(request, 'form_prod.html', {'form': form})



@login_required()
def delete_prod(request, id):
    produtos = get_object_or_404(CadProd, pk=id)

    if request.method == 'POST':
        produtos.delete()
        return redirect('prod_list')

    return render(request, 'delete_prod.html', {'produtos':produtos})


