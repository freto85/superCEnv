from django import forms
from news.models import News, Comment

class NewsForm(forms.ModelForm):

    class Meta():
        model = News
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'texinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
