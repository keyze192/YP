from django import forms
from django.utils import timezone
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['service', 'comment']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self._user
        instance.status = 0
        instance.created_at = timezone.now()
        
        if commit:
            instance.save()
        return instance