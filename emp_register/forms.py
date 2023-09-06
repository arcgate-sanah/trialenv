from django import forms
from .models import Salary


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Salary
        fields = ("employee", "department", "name", "startDate", "endDate")
        labels = {
            "employee": "Employee",
            "department": "Department",
            "name": "Name",
            "startDate": "Start Date",
            "endDate": "End Date"
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        
        # Customize the widget for the 'startDate' field to use DateInput
        self.fields['startDate'].widget = forms.DateInput(attrs={'type': 'date'})

        # Set the format for displaying the date (optional)
        self.fields['startDate'].input_formats = ['%Y-%m-%d']  # Change the format as needed

        self.fields['endDate'].widget = forms.DateInput(attrs={'type': 'date'})

        # Set the format for displaying the date (optional)
        self.fields['endDate'].input_formats = ['%Y-%m-%d'] 