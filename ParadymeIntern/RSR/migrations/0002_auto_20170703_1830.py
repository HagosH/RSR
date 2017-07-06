# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-03 18:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RSR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AwardName', models.CharField(max_length=100, verbose_name='Award Name')),
                ('AwardDescriptioin', models.CharField(max_length=1000, verbose_name='Award Description')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_column='Name', max_length=20, verbose_name='Name')),
                ('Description', models.CharField(db_column='Description', max_length=30, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Clearence',
            fields=[
                ('ClearenceLevel', models.CharField(db_column='ClearenceLevel', max_length=30, primary_key=True, serialize=False, verbose_name='Clearence Level')),
            ],
        ),
        migrations.CreateModel(
            name='Clubs_Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CHName', models.CharField(max_length=100, verbose_name='Club and Hobby Name')),
                ('CHDesc', models.CharField(max_length=100, verbose_name='Club and Hobby Description')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=100, verbose_name='Company Name')),
            ],
        ),
        migrations.CreateModel(
            name='Coursework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_column='Name', max_length=50, verbose_name='Coursework Name')),
                ('Desc', models.CharField(db_column='Desc', max_length=50, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageSpoken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(db_column='Language', max_length=20, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_column='Name', max_length=50, verbose_name='Name')),
                ('Dept', models.CharField(db_column='Dept', max_length=50, verbose_name='Department Name')),
                ('MajorMinor', models.CharField(db_column='Major/Minor', max_length=50, verbose_name='Major/Minor')),
            ],
        ),
        migrations.CreateModel(
            name='OCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resume', models.FileField(upload_to='/PreOCR')),
                ('CreationDate', models.DateTimeField(verbose_name='Creation')),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
                ('Address', models.CharField(max_length=50, verbose_name='Address')),
                ('ZipCode', models.IntegerField()),
                ('State', models.CharField(max_length=25, verbose_name='State')),
                ('PhoneNumber', models.CharField(max_length=50, verbose_name='Phone')),
                ('Resume', models.FileField(upload_to='/resumes')),
                ('CreationDate', models.DateTimeField(verbose_name='Creation')),
                ('LastUpdated', models.DateTimeField(blank=True, null=True, verbose_name='Update')),
                ('Linkden', models.CharField(max_length=70, verbose_name='Linkden')),
                ('GitHun', models.CharField(max_length=70, verbose_name='GitHub')),
                ('TypeResume', models.CharField(choices=[('Employee', 'Current Employee'), ('Prospective', 'Prospective Employee')], default='Prospective', max_length=50)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person_Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AwardName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Awards')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CertID', models.ForeignKey(db_column='CertID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Certificate')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Clearence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClearenceLevel', models.ForeignKey(db_column='ClearenceLevel', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Clearence')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Clubs_Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CHName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Clubs_Hobbies')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default=None, max_length=100, verbose_name='Title')),
                ('ExperienceOnJob', models.CharField(default=None, max_length=300, verbose_name='Experience on Job')),
                ('StartDate', models.DateField(default=3, verbose_name='Start Date')),
                ('EndDate', models.DateField(default=3, verbose_name='End Date')),
                ('CompanyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Company')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LangID', models.ForeignKey(db_column='LangID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.LanguageSpoken')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('YearsOfExperience', models.CharField(db_column='YrsOfExp', max_length=3, verbose_name='Years Of Experience')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_to_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(db_column='CourseID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Coursework')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_to_School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GradDate', models.CharField(db_column='GradDate', max_length=20, verbose_name='Grad Date')),
                ('GPA', models.CharField(db_column='GPA', max_length=20, verbose_name='GPA')),
                ('CourseID', models.ForeignKey(db_column='CourseID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Coursework')),
                ('MajorID', models.ForeignKey(db_column='MajorID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Major')),
                ('PersonID', models.ForeignKey(db_column='PersonID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Volunteering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Person')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_column='Name', max_length=50, verbose_name='School Name')),
                ('GradorUndergrad', models.CharField(db_column='GradorUndergrad', max_length=50, verbose_name='Graduate or Undergraduate')),
            ],
        ),
        migrations.CreateModel(
            name='SideProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjectName', models.CharField(db_column='ProjectName', max_length=20, verbose_name='Project Name')),
                ('ProjectDesc', models.CharField(db_column='ProjectDesc', max_length=50, verbose_name='Project Description')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SkillsName', models.CharField(db_column='SkillsName', max_length=20, verbose_name='Skills Name')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VounName', models.CharField(max_length=100, verbose_name='Volunteering Name')),
                ('VolunDesc', models.CharField(max_length=1000, verbose_name='Volunteering Description')),
            ],
        ),
        migrations.AddField(
            model_name='person_volunteering',
            name='VolunName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.Volunteering'),
        ),
        migrations.AddField(
            model_name='person_to_school',
            name='SchoolID',
            field=models.ForeignKey(db_column='SchoolID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.School'),
        ),
        migrations.AddField(
            model_name='person_skills',
            name='SkillsID',
            field=models.ForeignKey(db_column='SkillsID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.Skills'),
        ),
        migrations.AddField(
            model_name='person_side',
            name='SideID',
            field=models.ForeignKey(db_column='SideID', on_delete=django.db.models.deletion.DO_NOTHING, to='RSR.SideProject'),
        ),
        migrations.AddField(
            model_name='ocr',
            name='NewPath',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RSR.Person'),
        ),
    ]