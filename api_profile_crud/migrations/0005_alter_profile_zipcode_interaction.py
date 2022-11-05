# Generated by Django 4.0.5 on 2022-11-03 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_profile_crud', '0004_remove_profile_img_alter_profile_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_left', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_left', to='api_profile_crud.profile')),
                ('profile_right', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_right', to='api_profile_crud.profile')),
            ],
        ),
    ]
