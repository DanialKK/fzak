from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
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
            'name': forms.TextInput(attrs={
                'placeholder': 'مثلاً علی رضایی',
                'class': 'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm '
                         'focus:border-blue-600 focus:ring-1 focus:ring-blue-600'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '09xxxxxxxxx',
                'class': 'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm '
                         'focus:border-blue-600 focus:ring-1 focus:ring-blue-600'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@email.com',
                'class': 'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm '
                         'focus:border-blue-600 focus:ring-1 focus:ring-blue-600'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'متن پیام شما',
                'rows': 4,
                'class': 'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm '
                         'focus:border-blue-600 focus:ring-1 focus:ring-blue-600'
            }),
        }
