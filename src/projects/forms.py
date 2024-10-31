from django import forms
from .models import Project

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'handle', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white ',
                'placeholder': 'Enter project title'
            }),
            'handle': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Enter project handle'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Enter project description',
                'rows': 4,
            }),
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'handle', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Update project title'
            }),
            'handle': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Update project handle'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Update project description',
                'rows': 4,
            }),
        }
