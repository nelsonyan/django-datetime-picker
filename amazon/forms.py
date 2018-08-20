from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput, DatePickerInput
from django import forms
from amazon.models import IssueTracking

class IssueInput(forms.ModelForm):
    class Meta:
        model = IssueTracking
        fields = '__all__'
        widgets = {
            'date_time': DatePickerInput(
            options={
                    "format": "MM/DD/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
        }
