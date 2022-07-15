from django import forms
from .models import Contractor, Company, Contract, ProjectManager, MonthStatus, Status


class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor
        fields = '__all__'


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class PMForm(forms.ModelForm):

    class Meta:
        model = ProjectManager
        fields = '__all__'


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = '__all__'


class MonthStatusForm(forms.ModelForm):

    class Meta:
        model = MonthStatus
        fields = ('performance', 'date', 'certificate_of_completion', )


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('comment', )
