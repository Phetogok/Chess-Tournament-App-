from django import forms
from .models import Tournament, News, Player, AdminProfile
from django.contrib.auth.models import User

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'location', 'description', 'document', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Tournament Name'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'type': 'datetime-local'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Tournament Location'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 4,
                'placeholder': 'Tournament Description'
            }),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'News Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'rows': 6,
                'placeholder': 'News Content'
            }),
        }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'rating', 'role', 'availability', 'profile_img', 'specialty']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'availability': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'specialty': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Specialty (for coaches)'
            }),
        }