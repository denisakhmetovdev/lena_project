from django.urls import path
from .views import home, add_all, add_contractor, add_company, add_pm, add_contract, contract_detail, add_month_status,\
    add_status


urlpatterns = [
    path('add_all/', add_all, name='add_all'),
    path('contract_detail/<int:contract_id>/', contract_detail, name='contract_detail'),
    path('add_contractor/', add_contractor, name='+contractor'),
    path('add_company/', add_company, name='+company'),
    path('add_project_manager/', add_pm, name='add_pm'),
    path('add_contract/', add_contract, name='+contract'),
    path('add_month_status/<int:contract_id>/', add_month_status, name='+month_status'),
    path('add_status/<int:contract_id>/', add_status, name='+status'),
    path('', home, name='home')
]
