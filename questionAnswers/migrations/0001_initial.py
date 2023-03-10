# Generated by Django 4.1.3 on 2022-12-03 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('describe_question', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('solved', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='questionAnswers.question')),
            ],
        ),
    ]
