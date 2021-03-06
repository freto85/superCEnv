# Generated by Django 3.0.2 on 2020-02-04 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('grammar_skills', models.IntegerField(default=0)),
                ('listening_skills', models.IntegerField(default=0)),
                ('writing_skills', models.IntegerField(default=0)),
                ('vocabulary_skills', models.IntegerField(default=0)),
                ('oral_skills', models.IntegerField(default=0)),
                ('reading_skills', models.IntegerField(default=0)),
                ('songs_listened', models.IntegerField(default=0)),
                ('songs_sang', models.IntegerField(default=0)),
                ('stories_read', models.IntegerField(default=0)),
                ('books_finished', models.IntegerField(default=0)),
                ('words_learned', models.IntegerField(default=0)),
                ('irregular_verbs', models.IntegerField(default=0)),
                ('talking_time', models.IntegerField(default=0)),
                ('no_spanish_time', models.IntegerField(default=0)),
                ('writing_assignments', models.IntegerField(default=0)),
                ('perfect_writing', models.BooleanField(default=False)),
                ('book_written', models.BooleanField(default=False)),
                ('monkey_island', models.BooleanField(default=False)),
                ('the_last_door', models.BooleanField(default=False)),
                ('to_the_moon', models.BooleanField(default=False)),
                ('oxenfree', models.BooleanField(default=False)),
                ('valiant_hearts', models.BooleanField(default=False)),
                ('walter_mitty', models.BooleanField(default=False)),
                ('big_fish', models.BooleanField(default=False)),
                ('warm_bodies', models.BooleanField(default=False)),
                ('the_help', models.BooleanField(default=False)),
                ('reign_over_me', models.BooleanField(default=False)),
                ('phonemes_learned', models.IntegerField(default=0)),
                ('talked_to_native', models.BooleanField(default=False)),
                ('cinema_day', models.BooleanField(default=False)),
                ('escape_room', models.BooleanField(default=False)),
                ('every_event', models.BooleanField(default=False)),
                ('game_of_life_won', models.IntegerField(default=0)),
                ('scrabble_points', models.IntegerField(default=0)),
                ('heave_ho_worlds', models.IntegerField(default=0)),
                ('monopoly_won', models.IntegerField(default=0)),
                ('max_dart_points', models.IntegerField(default=0)),
                ('human_fall_flat_worlds', models.IntegerField(default=0)),
                ('jenga_won', models.IntegerField(default=0)),
                ('stick_fight_won', models.IntegerField(default=0)),
                ('operation_won', models.IntegerField(default=0)),
                ('pikuniku_levels', models.IntegerField(default=0)),
                ('battleship_won', models.IntegerField(default=0)),
                ('lovers_levels', models.IntegerField(default=0)),
                ('defused_bomb', models.BooleanField(default=False)),
                ('chemistry_performed', models.BooleanField(default=False)),
                ('baked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
