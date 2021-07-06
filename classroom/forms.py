from django import forms
from .models import Class
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class EditMember(forms.ModelForm):
    student = forms.Textarea()
    ta = forms.Textarea()
    teacher = forms.Textarea()

    class Meta:
        model = Class
        fields = ['student', 'ta', 'teacher']