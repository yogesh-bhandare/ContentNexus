from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Enter item title',
            }),
        }

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'status', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Enter item title',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Enter description',
                'rows': 4,
            }),
        }

class ItemInlineForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
                'placeholder': 'Enter item title',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            }),
        }

class ItemPatchForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-800 text-white',
            'placeholder': 'Enter item title',
        })
    )
    status = forms.CharField(
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
