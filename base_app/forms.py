from django import forms
from django.forms import SelectDateWidget
import datetime
from dateutil.relativedelta import relativedelta

from base_app.models import Contracts


# class DateInput(forms.DateInput):
#     input_type = 'date'


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

    # def __init__(self, filial_slug=None, **kwargs):
    #     super(ContractEditForm, self).__init__(**kwargs)
    #     if filial_slug:
    #         self.fields['filial'].queryset = Contracts.objects.filter(filial__slug=filial_slug)


class ReportFiltersDateForm(forms.Form):
    today = datetime.date.today()
    # def __init__(self, *args, **kwargs):
    #     super(ReportFiltersDateForm, self).__init__(*args, **kwargs)
    #     today = datetime.date.today()
    #     self.first_day = today.replace(day=1) - relativedelta(months=1)
    #     self.last_day = today.replace(day=1) - datetime.timedelta(days=1)
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
        # self.fields['file'].widget.attrs['class'] = 'inp_open_file'
        # self.fields['file'].widget.attrs['accept'] = '.xls,.xlsx'
        self.fields['contract'].queryset = submenu

    contract = forms.ModelChoiceField(
        queryset=Contracts.objects.all(),
        label=False,
        # help_text='Выберите контракт'
    )
    # file = forms.FileField(
    #     label=False
    # )
