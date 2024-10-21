# Generated by Django 4.2 on 2024-10-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_user_managers_alter_kala_pic0_alter_kala_pic1_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic0',
            field=models.ImageField(default='no-image.jpg', height_field='image_height', upload_to='static/images/products/20241017-140355', width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20241017 - 140355'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20241017 - 140355'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20241017 - 140355'),
        ),
        migrations.AlterField(
            model_name='kala',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20241017 - 140355'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, default='no-image.jpg', height_field='image_height', null=True, upload_to='static/images/posts/20241017-140355', width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='sold',
            name='FollowUpCode',
            field=models.CharField(default='9120241017140355', max_length=20),
        ),
        migrations.AlterField(
            model_name='sold',
            name='sent',
            field=models.CharField(choices=[('T', 'Package sent'), ('F', 'Package Wait for send'), ('B', 'Back to Store')], default='F', help_text='Is package sent?', max_length=1, verbose_name='Send Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='no-image.jpg', height_field='image_height', upload_to='static/images/profile/20241017-140355', width_field='image_width'),
        ),
    ]
