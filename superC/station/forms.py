from django import forms
from .models import Document, Audio
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','description', 'document')

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title','description', 'audio_file')
