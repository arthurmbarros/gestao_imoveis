from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from appgestaoimoveis.forms import ContratosForm
from appgestaoimoveis.forms import InquilinosForm
from appgestaoimoveis.models import Contratos
from appgestaoimoveis.models import Inquilinos
from appgestaoimoveis.models import Imoveis
from appgestaoimoveis.forms import ImoveisForm

@login_required
def home(request):
    data = {}
    search = request.GET.get("search")
    if search:
        data["db"] = Contratos.objects.filter(modelo__icontains=search)
    else:
        data["db"] = Contratos.objects.all()
    x = 0
    for dbs in data["db"]:
        x = x + dbs.valor_aluguel
    data["x"] = x
    return render(request, "index.html", data)

@login_required    
def form(request):
    data = {}
    data["form"] = ContratosForm()
    return render(request, "form.html", data)


@login_required
def create(request):
    form = ContratosForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect("home")

@login_required
def edit(request, pk):
    data = {}
    data["db"] = Contratos.objects.get(pk=pk)
    data["form"] = ContratosForm(instance=data["db"])
    return render(request, "form.html", data)

@login_required
def update(request, pk):
    data = {}
    data["db"] = Contratos.objects.get(pk=pk)
    form = ContratosForm(request.POST or None, instance=data["db"])
    if form.is_valid():
        form.save()
        return redirect("home")

@login_required    
def delete(request, pk):
    db = Contratos.objects.get(pk=pk)
    db.delete()
    return redirect("home")

@login_required
def inquilinos(request):
    data = {}
    data["inquilinos"] = Inquilinos.objects.all()
    return render(request, "inquilinos.html", data)

@login_required
def forminquilinos(request):
    data = {}
    data["forminquilinos"] = InquilinosForm()
    return render(request, "forminquilinos.html", data)

@login_required
def createinquilinos(request):
    form = InquilinosForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect("inquilinos")

@login_required
def deleteinquilinos(request, pk):
    db = Inquilinos.objects.get(pk=pk)
    db.delete()
    return redirect("inquilinos")

@login_required
def editinquilinos(request, pk):
    data = {}
    data["db"] = Inquilinos.objects.get(pk=pk)
    data["forminquilinos"] = InquilinosForm(instance=data["db"])
    return render(request, "forminquilinos.html", data)

@login_required
def updateinquilinos(request, pk):
    data = {}
    data["forminquilinos"] = Inquilinos.objects.get(pk=pk)
    form = InquilinosForm(request.POST or None, instance=data["forminquilinos"])
    if form.is_valid():
        form.save()
        return redirect("inquilinos")

@login_required    
def imoveis(request):
    data = {}
    data["imoveis"] = Imoveis.objects.all()
    return render(request, "imoveis.html", data)

@login_required
def formimoveis(request):
    data = {}
    data["formimoveis"] = ImoveisForm()
    return render(request, "formimoveis.html", data)

@login_required
def createimoveis(request):
    form = ImoveisForm(request.POST or None)
    if  form.is_valid():
        form.save()
        return redirect("imoveis")

@login_required
def deleteimoveis(request, pk):
    db = Imoveis.objects.get(pk=pk)
    db.delete()
    return redirect("imoveis")

@login_required
def editimoveis(request, pk):
    data = {}
    data["db"] = Imoveis.objects.get(pk=pk)
    data["formimoveis"] = ImoveisForm(instance=data["db"])
    return render(request, "formimoveis.html", data)

@login_required
def updateimoveis(request, pk):
    data = {}
    data["formimoveis"] = Imoveis.objects.get(pk=pk)
    form = ImoveisForm(request.POST or None, instance=data["formimoveis"])
    if form.is_valid():
        form.save()
        return redirect("imoveis")

@login_required
def totalalugueis(request):
    total_alugueis = Contratos.objects.aggregate(Sum('valor_aluguel'))['valor_aluguel__sum']
    print(f'Total de Alugueis: {total_alugueis}')
    return render(request, 'index.html', {'total_alugueis': total_alugueis})
