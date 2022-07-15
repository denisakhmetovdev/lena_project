from django.shortcuts import render, redirect
from .models import *
from .forms import ContractorForm, CompanyForm, ContractForm, PMForm, MonthStatusForm, StatusForm
from datetime import date


def home(request):
    contracts = Contract.objects.all()
    context = {
        'contracts': contracts
    }
    return render(request, 'work/home.html', context)


def add_all(request):
    return render(request, 'work/add_all.html')


def add_contractor(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_all)
    else:
        form = ContractorForm
        context = {
            'form': form
        }
        return render(request, 'work/add_contractor.html', context)


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_all)
    else:
        form = CompanyForm
        context = {
            'form': form
        }
        return render(request, 'work/add_company.html', context)


def add_pm(request):
    if request.method == 'POST':
        form = PMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_all)
    else:
        form = PMForm
        context = {
            'form': form
        }
        return render(request, 'work/add_company.html', context)


def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_all)
    else:
        form = ContractForm
        context = {
            'form': form
        }
        return render(request, 'work/add_contract.html', context)


def contract_detail(request, contract_id):
    contract = Contract.objects.get(pk=contract_id)
    month_statuses = MonthStatus.objects.filter(contract=contract)
    statuses = Status.objects.filter(contract=contract)
    sup_contract = SupplementaryContract.objects.filter(contract=contract)
    context = {
        'contract': contract,
        'month_statuses': month_statuses,
        'statuses': statuses,
        'sup_contract': sup_contract
    }
    return render(request, 'work/contract_detail.html', context)


def add_month_status(request, contract_id):
    if request.method == 'POST':
        form = MonthStatusForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.contract = Contract.objects.get(pk=contract_id)
            post.save()
            return redirect(contract_detail, contract_id=contract_id)
    else:
        form = MonthStatusForm
        context = {
            'form': form
        }
        return render(request, 'work/add_month_status.html', context)


def add_status(request, contract_id):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.contract = Contract.objects.get(pk=contract_id)
            post.save()
            return redirect(contract_detail, contract_id=contract_id)
    else:
        form = StatusForm
        context = {
            'form': form
        }
        return render(request, 'work/add_status.html', context)
