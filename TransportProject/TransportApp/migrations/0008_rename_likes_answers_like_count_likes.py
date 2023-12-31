# Generated by Django 4.2.6 on 2023-11-01 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TransportApp', '0007_alter_answers_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='likes',
            new_name='like_count',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.answers')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.questions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.registration')),
            ],
        ),
    ]
