from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
                email = self.normalize_email(email),
                username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    #Personal Data
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Medals
    grammar_skills = models.IntegerField(default=0)
    listening_skills = models.IntegerField(default=0)
    writing_skills = models.IntegerField(default=0)
    vocabulary_skills = models.IntegerField(default=0)
    oral_skills = models.IntegerField(default=0)
    reading_skills = models.IntegerField(default=0)

    #Trophies
    songs_listened = models.IntegerField(default=0)
    songs_sang = models.IntegerField(default=0)
    stories_read = models.IntegerField(default=0)
    books_finished = models.IntegerField(default=0)
    words_learned = models.IntegerField(default=0)
    irregular_verbs = models.IntegerField(default=0)
    talking_time = models.IntegerField(default=0)
    no_spanish_time =  models.IntegerField(default=0)
    writing_assignments = models.IntegerField(default=0)
    perfect_writing = models.BooleanField(default=False)
    book_written = models.BooleanField(default=False)

    #Stickers
    monkey_island = models.BooleanField(default=False)
    the_last_door = models.BooleanField(default=False)
    to_the_moon = models.BooleanField(default=False)
    oxenfree = models.BooleanField(default=False)
    valiant_hearts = models.BooleanField(default=False)

    walter_mitty = models.BooleanField(default=False)
    big_fish = models.BooleanField(default=False)
    warm_bodies = models.BooleanField(default=False)
    the_help = models.BooleanField(default=False)
    reign_over_me = models.BooleanField(default=False)

    phonemes_learned = models.IntegerField(default=0)
    talked_to_native = models.BooleanField(default=False)
    cinema_day = models.BooleanField(default=False)
    escape_room = models.BooleanField(default=False)
    every_event = models.BooleanField(default=False)

    #Roadmap
    game_of_life_won = models.IntegerField(default=0)
    scrabble_points = models.IntegerField(default=0)
    heave_ho_worlds = models.IntegerField(default=0)
    monopoly_won = models.IntegerField(default=0)
    max_dart_points = models.IntegerField(default=0)
    human_fall_flat_worlds = models.IntegerField(default=0)
    jenga_won = models.IntegerField(default=0 )
    stick_fight_won = models.IntegerField(default=0)
    operation_won = models.IntegerField(default=0)
    pikuniku_levels = models.IntegerField(default=0)
    battleship_won = models.IntegerField(default=0 )
    lovers_levels = models.IntegerField(default=0 )
    defused_bomb = models.BooleanField(default=False)
    chemistry_performed = models.BooleanField(default=False)
    baked = models.BooleanField(default=False)

    #####################################################################
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('accounts:detail_account',kwargs={'pk':self.pk})

get_user = get_user_model()

class MessageData(models.Model):
        content = models.TextField()

        def get_absolute_url(self):
            return reverse('accounts:messages',kwargs={'username':get_user.username,'pk':self.pk})

class Message(models.Model):
        sender = models.ForeignKey(get_user, related_name="user_send",on_delete=models.CASCADE, null=True)
        receiver = models.ForeignKey(get_user, related_name="user_get",on_delete=models.CASCADE, null=True)
        message_dataID = models.ForeignKey(MessageData, related_name="message_data",on_delete=models.CASCADE, null=True)
        created_at = models.DateTimeField(default=timezone.now)

        def get_absolute_url(self):
                return reverse('accounts:messages', kwargs={'pk':sens.pk})

        class Meta:
            unique_together = ('sender', 'receiver')
