# Generated by Django 4.0.4 on 2022-06-14 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Team_Leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('Team_Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team', models.CharField(choices=[('Developer', 'Developer'), ('Tester', 'Tester'), ('Busness analyst', 'Busness analyst'), ('Technical lead', 'Technical lead')], max_length=100)),
                ('Status', models.CharField(choices=[('Assigned', 'Assigned'), ('Under review', 'Under review'), ('Progress', 'Progress'), ('Done', 'Done')], default=1, max_length=100)),
                ('Started_at', models.DateField()),
                ('Completed_at', models.DateField()),
                ('Team_Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]