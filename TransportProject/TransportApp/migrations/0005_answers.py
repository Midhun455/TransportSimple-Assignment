# Generated by Django 4.2.6 on 2023-10-31 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TransportApp', '0004_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.questions')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.registration')),
            ],
        ),
    ]
