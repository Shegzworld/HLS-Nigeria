# Generated by Django 5.0.7 on 2024-10-24 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=255)),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DosageForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DosageForm', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PharmacyGrouping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PharmacyGrouping', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='product',
            name='suitable_for',
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
        migrations.RenameField(
            model_name='lifestyle',
            old_name='name',
            new_name='LifestyleType',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='benefits',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='lifestyle_compatibility',
            new_name='lifestyle',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(null=True, upload_to='product_images/main'),
        ),
        migrations.AddField(
            model_name='product',
            name='side_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/secondary'),
        ),
        migrations.AddField(
            model_name='product',
            name='side_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/secondary'),
        ),
        migrations.AddField(
            model_name='product',
            name='side_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/secondary'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='age_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NT_gallery.agerange'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(to='NT_gallery.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='dosage_form',
            field=models.ManyToManyField(to='NT_gallery.dosageform'),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.ManyToManyField(to='NT_gallery.gender'),
        ),
        migrations.AddField(
            model_name='product',
            name='lifestyle_rating',
            field=models.ManyToManyField(to='NT_gallery.lifestylerating'),
        ),
        migrations.AddField(
            model_name='product',
            name='pharmacy_grouping',
            field=models.ManyToManyField(to='NT_gallery.pharmacygrouping'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='NT_gallery.product'),
        ),
        migrations.AddField(
            model_name='productreview',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='HealthGoal',
        ),
        migrations.DeleteModel(
            name='MedicalCondition',
        ),
    ]
