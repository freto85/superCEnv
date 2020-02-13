from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User, Message, MessageData

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('first_name','last_name','username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Username'
        self.fields['email'].label = "E-Mail Account"


class AccountUpdatePersonalInfoForm(forms.ModelForm):

    class Meta:
        fields = ('email','username','first_name','last_name','email')
        model = User

class AccountUpdateMedalsForm(forms.ModelForm):

    class Meta:
        fields = ('grammar_skills','listening_skills','writing_skills','vocabulary_skills','oral_skills','reading_skills')
        model = User

class AccountUpdateTrophiesForm(forms.ModelForm):

    class Meta:
        fields = ('songs_listened','songs_sang','stories_read','books_finished','words_learned','irregular_verbs','talking_time','no_spanish_time','writing_assignments','perfect_writing','book_written')
        model = User

class AccountUpdateStickersForm(forms.ModelForm):

    class Meta:
        fields = ('monkey_island','the_last_door','to_the_moon','oxenfree','valiant_hearts','walter_mitty','big_fish','warm_bodies','the_help','reign_over_me','phonemes_learned','talked_to_native','cinema_day','escape_room','every_event')
        model = User

class AccountUpdateRoadmapForm(forms.ModelForm):

    class Meta:
        fields = ('game_of_life_won','scrabble_points','heave_ho_worlds','monopoly_won','max_dart_points','human_fall_flat_worlds','jenga_won','stick_fight_won','operation_won','pikuniku_levels','battleship_won','lovers_levels','defused_bomb','chemistry_performed','baked')
        model = User

class NewMessageForm(forms.ModelForm):
    class Meta:
        fields = ('receiver',)
        model = Message

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['receiver'].label = 'Send it to:'

class MessageForm(forms.ModelForm):

    class Meta:
        fields = ('content',)
        model = MessageData

        widgets = {
            'content':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
            }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['content'].label = 'Type a message here!'
