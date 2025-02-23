# apps/service_requests/forms.py

from django import forms
from .models import ServiceRequest, ServiceRequestComment, ServiceRequestAttachment

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['category', 'title', 'description', 'priority', 'location', 'preferred_date', 'preferred_time']
        widgets = {
            'preferred_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'preferred_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('title'):
            raise forms.ValidationError('Title is required')
        if not cleaned_data.get('description'):
            raise forms.ValidationError('Description is required')
        if not cleaned_data.get('category'):
            raise forms.ValidationError('Category is required')
        return cleaned_data
    
class ServiceRequestCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add a comment...'}),
        }

class ServiceRequestAttachmentForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestAttachment
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brief description of the attachment'
            })
        }

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestAttachment
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brief description of the attachment'
            })
        }
