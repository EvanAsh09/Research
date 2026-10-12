from django import forms
from .models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["title", "course", "due_date", "priority", "notes"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }