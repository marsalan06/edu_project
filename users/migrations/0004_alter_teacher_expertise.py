# Generated by Django 4.2.2 on 2023-07-08 09:57

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_teacher_expertise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='expertise',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('phy', 'Physics'), ('chem', 'Chemistry'), ('math', 'Mathematics'), ('comp', 'Computer Science'), ('humn', 'Humanities'), ('bio', 'Biology'), ('zoo', 'Zoology'), ('bot', 'Botany')], max_length=255),
        ),
    ]
