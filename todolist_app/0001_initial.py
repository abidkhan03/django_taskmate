from django.db import migrations, models

class Migrations(migrations.Migration):
    intial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name = "TaskList", 
            fields = [
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]