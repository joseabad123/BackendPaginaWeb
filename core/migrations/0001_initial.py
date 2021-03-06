# Generated by Django 2.1.7 on 2019-11-30 06:18

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Content_Media',
            fields=[
                ('content_media_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=500)),
                ('content_id', models.ForeignKey(db_column='content_id', on_delete=django.db.models.deletion.PROTECT, to='core.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('place', models.CharField(max_length=255)),
                ('link_form', models.CharField(max_length=255)),
                ('url_info', models.CharField(max_length=255)),
                ('content_id', models.ForeignKey(db_column='content_id', on_delete=django.db.models.deletion.PROTECT, to='core.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_Contact',
            fields=[
                ('group_contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group_Event',
            fields=[
                ('group_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(db_column='event_id', on_delete=django.db.models.deletion.PROTECT, to='core.Event')),
                ('group_id', models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.PROTECT, to='core.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Category',
            fields=[
                ('item_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.PROTECT, to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('order', models.IntegerField()),
                ('item_category_id', models.ForeignKey(db_column='item_category_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('first_last_name', models.CharField(max_length=255)),
                ('second_last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person_Contact',
            fields=[
                ('person_contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=255)),
                ('contact_type_id', models.ForeignKey(db_column='contact_type_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category')),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.PROTECT, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Media',
            fields=[
                ('person_media_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=255)),
                ('item_category_id', models.ForeignKey(db_column='item_category_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category')),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.PROTECT, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Role',
            fields=[
                ('person_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.PROTECT, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Section',
            fields=[
                ('person_section_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_id', models.ForeignKey(db_column='person_id', on_delete=django.db.models.deletion.PROTECT, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('requirement_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('university_career_id', models.ForeignKey(db_column='university_career_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Matter',
            fields=[
                ('subject_matter_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('university_career_id', models.ForeignKey(db_column='university_career_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category')),
            ],
        ),
        migrations.AddField(
            model_name='requirement',
            name='subject_matter_id',
            field=models.ForeignKey(db_column='subject_matter_id', on_delete=django.db.models.deletion.PROTECT, related_name='subject_matter_id_related_name', to='core.Subject_Matter'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='subject_matter_requeriment_id',
            field=models.ForeignKey(db_column='subject_matter_requirement_id', on_delete=django.db.models.deletion.PROTECT, related_name='subject_matter_requeriment_id_related_name', to='core.Subject_Matter'),
        ),
        migrations.AddField(
            model_name='person_section',
            name='section_id',
            field=models.ForeignKey(db_column='section_id', on_delete=django.db.models.deletion.PROTECT, to='core.Section'),
        ),
        migrations.AddField(
            model_name='person_role',
            name='role_id',
            field=models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.PROTECT, to='core.Role'),
        ),
        migrations.AddField(
            model_name='person_role',
            name='university_career_id',
            field=models.ForeignKey(db_column='university_career_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='group_contact',
            name='contact_type_id',
            field=models.ForeignKey(db_column='contact_type_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='group_contact',
            name='group_id',
            field=models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.PROTECT, to='core.Group'),
        ),
        migrations.AddField(
            model_name='group',
            name='university_career_id',
            field=models.ForeignKey(db_column='university_career_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='content_media',
            name='item_category_id',
            field=models.ForeignKey(db_column='item_category_id', on_delete=django.db.models.deletion.PROTECT, to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='content',
            name='academic_period_id',
            field=models.ForeignKey(db_column='academic_period_id', on_delete=django.db.models.deletion.PROTECT, related_name='academic_period_id_related_name', to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='content',
            name='content_type_id',
            field=models.ForeignKey(db_column='contact_type_id', on_delete=django.db.models.deletion.PROTECT, related_name='content_type_id_related_name', to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='content',
            name='university_career_id',
            field=models.ForeignKey(db_column='university_career_id', on_delete=django.db.models.deletion.PROTECT, related_name='university_career_id_related_name', to='core.Item_Category'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='person_id',
            field=models.OneToOneField(db_column='person_id', on_delete=django.db.models.deletion.PROTECT, to='core.Person'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
