from django import forms
from django.forms import SelectDateWidget
import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404

from base_app.models import Contracts


class PeriodForm(forms.Form):
    today = datetime.date.today()
    start_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'value': today.replace(day=1) - relativedelta(months=1)
    }))
    end_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'value': today.replace(day=1) - datetime.timedelta(days=1)
    }))


class ContractEditForm(forms.ModelForm):
    class Meta:
        model = Contracts
        exclude = ('name', 'slug',)


class ReportFiltersDateForm(forms.Form):
    today = datetime.date.today()
    start_date = forms.DateField(input_formats='%Y,%m,%d', widget=SelectDateWidget(),
                                 label='Start Date',
                                 initial=today.replace(day=1) - relativedelta(months=1)
                                 )
    end_date = forms.DateField(input_formats='%Y,%m,%d', widget=SelectDateWidget(),
                               label='End Date',
                               initial=today.replace(day=1) - datetime.timedelta(days=1)
                               )


class FileUploadForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'inp_open_file'
        self.fields['file'].widget.attrs['accept'] = '.xls,.xlsx'

    file = forms.FileField(
        label=False
    )


class ContractsForm(forms.Form):
    def __init__(self, submenu, **kwargs):
        super(ContractsForm, self).__init__(**kwargs)
        self.fields['contract'].widget.attrs['class'] = 'inp_open_file'
        self.fields['contract'].widget.attrs['id'] = 'contract'
        self.fields['contract'].queryset = submenu
    contract = forms.ModelChoiceField(
        queryset=Contracts.objects.all().order_by('name').values_list('slug', 'name'),
        label=False,
    )
