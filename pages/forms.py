from django import forms
from .models import Lead

class Leadform(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'message']
        labels = {
            'name': 'نام و نام خانوادگی',
            'phone': 'شماره تماس',
            'email': 'ایمیل',
            'message': 'پیام شما',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'مثلاً علی رضایی'}),
            'phone': forms.TextInput(attrs={'placeholder': '09xxxxxxxxx'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@email.com'}),
            'message': forms.Textarea(attrs={'placeholder': 'متن پیام شما'}),
        }