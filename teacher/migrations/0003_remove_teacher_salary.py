from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
    ]
