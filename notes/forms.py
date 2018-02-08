from django import forms

from .models import Note

from rest_framework import serializers

class NoteForm(forms.ModelForm):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        #fields = ('note_title', 'note_text','owner')
        fields = ('note_title', 'note_text')

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )