from django import forms
from resources.models import MediaAudioModel,MediaImageModel,MediaVideoModel

class MediaVideoForm(forms.ModelForm):

    class Meta():
        model = MediaVideoModel
        fields = ('user','title','video_file','slug','description')

        widgets = {
            'title':forms.TextInput(attrs={'class':'texinputclass'}),
            'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class MediaImageForm(forms.ModelForm):
    class Meta:
        model = MediaImageModel
        fields = ('user','title','description', 'image_file')
        widgets = {
            'title':forms.TextInput(attrs={'class':'texinputclass'}),
            'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
            }
class MediaAudioForm(forms.ModelForm):
    class Meta:
        model = MediaAudioModel
        fields = ('user','title','description','audio_file')
        widgets = {
            'title':forms.TextInput(attrs={'class':'texinputclass'}),
            'description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
            }
