# Generated by Django 4.2.7 on 2023-12-10 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0002_alter_employee_created_at_alter_team_team_lead_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_lead_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_management.team'),
        ),
    ]
