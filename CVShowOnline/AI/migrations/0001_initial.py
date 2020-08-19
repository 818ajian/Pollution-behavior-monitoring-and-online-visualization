# Generated by Django 3.0.5 on 2020-07-17 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='age_distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_distribution_type', models.CharField(max_length=20, verbose_name='年龄段')),
                ('age_distribution_value', models.IntegerField(verbose_name='年龄段内人数')),
            ],
        ),
        migrations.CreateModel(
            name='crime_analyze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20, verbose_name='类型名称')),
                ('type_value', models.IntegerField(verbose_name='类型数量')),
            ],
        ),
        migrations.CreateModel(
            name='peolple_origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_province', models.CharField(max_length=20, verbose_name='省份名称')),
                ('people_count', models.IntegerField(verbose_name='省份数量')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='time_line_statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_line_statistics_type', models.CharField(max_length=20, verbose_name='时间段')),
                ('time_line_statistics_value', models.IntegerField(verbose_name='时间段内人数')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AI.Question')),
            ],
        ),
    ]