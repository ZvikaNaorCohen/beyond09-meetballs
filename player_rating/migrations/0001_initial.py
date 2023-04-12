# Generated by Django 4.2 on 2023-04-18 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRating',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('ball_game', models.CharField(
                    choices=[('Soccer', 'Soccer'),
                             ('Basketball', 'Basketball'),
                             ('Volleyball', 'Volleyball'),
                             ('Baseball', 'Baseball'),
                             ('Tennis', 'Tennis'),
                             ('Rugby', 'Rugby'),
                             ('Golf', 'Golf'),
                             ('Cricket', 'Cricket'),
                             ('Handball', 'Handball')],
                    max_length=100)),
                ('rating', models.IntegerField(
                    choices=[(0, 'Zero'),
                             (1, 'One'),
                             (2, 'Two'),
                             (3, 'Three'),
                             (4, 'Four'),
                             (5, 'Five'),
                             (6, 'Six'),
                             (7, 'Seven'),
                             (8, 'Eight'),
                             (9, 'Nine'),
                             (10, 'Ten')])),
                ('user_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='player.player')),
            ],
        ),
        migrations.AddConstraint(
            model_name='playerrating',
            constraint=models.UniqueConstraint(fields=('ball_game', 'user_id'), name='unique_player_rating'),
        ),
        migrations.AlterUniqueTogether(
            name='playerrating',
            unique_together={('ball_game', 'user_id')},
        ),
    ]