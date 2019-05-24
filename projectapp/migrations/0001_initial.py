# Generated by Django 2.0.6 on 2019-05-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BTable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(blank=True, max_length=40, null=True)),
                ('author', models.CharField(blank=True, max_length=40, null=True)),
                ('press', models.CharField(blank=True, max_length=40, null=True)),
                ('pricing', models.CharField(blank=True, max_length=40, null=True)),
                ('d_pricing', models.CharField(blank=True, max_length=40, null=True)),
                ('pic', models.ImageField(upload_to='pics')),
                ('putime', models.DateTimeField(blank=True, null=True)),
                ('column_10', models.CharField(blank=True, db_column='Column_10', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'b_table',
            },
        ),
        migrations.CreateModel(
            name='Indenttable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.CharField(blank=True, max_length=40, null=True)),
                ('money', models.CharField(blank=True, max_length=40, null=True)),
                ('column_8', models.CharField(blank=True, db_column='Column_8', max_length=10, null=True)),
                ('column_9', models.CharField(blank=True, db_column='Column_9', max_length=10, null=True)),
                ('column_10', models.CharField(blank=True, db_column='Column_10', max_length=10, null=True)),
                ('column_11', models.CharField(blank=True, db_column='Column_11', max_length=10, null=True)),
                ('column_12', models.CharField(blank=True, db_column='Column_12', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'indenttable',
            },
        ),
        migrations.CreateModel(
            name='MessBook',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('putime', models.DateTimeField(blank=True, null=True)),
                ('edition', models.CharField(blank=True, max_length=40, null=True)),
                ('pritime', models.DateTimeField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=40, null=True)),
                ('number', models.CharField(blank=True, max_length=40, null=True)),
                ('pagiation', models.CharField(blank=True, max_length=40, null=True)),
                ('format', models.CharField(blank=True, max_length=40, null=True)),
                ('paper', models.CharField(blank=True, max_length=40, null=True)),
                ('pack', models.CharField(blank=True, max_length=40, null=True)),
                ('impression', models.CharField(blank=True, max_length=40, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('suit', models.CharField(blank=True, max_length=40, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('column_16', models.CharField(blank=True, db_column='Column_16', max_length=10, null=True)),
                ('column_17', models.CharField(blank=True, db_column='Column_17', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'mess_book',
            },
        ),
        migrations.CreateModel(
            name='OneClassify',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('z_name', models.CharField(blank=True, max_length=40, null=True)),
                ('column_3', models.CharField(blank=True, db_column='Column_3', max_length=10, null=True)),
                ('column_4', models.CharField(blank=True, db_column='Column_4', max_length=10, null=True)),
                ('column_5', models.CharField(blank=True, db_column='Column_5', max_length=10, null=True)),
                ('column_6', models.CharField(blank=True, db_column='Column_6', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'one_classify',
            },
        ),
        migrations.CreateModel(
            name='SsClass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('one_head', models.CharField(blank=True, max_length=40, null=True)),
                ('two_head', models.CharField(blank=True, max_length=40, null=True)),
                ('column_4', models.CharField(blank=True, db_column='Column_4', max_length=10, null=True)),
                ('column_7', models.CharField(blank=True, db_column='Column_7', max_length=10, null=True)),
                ('column_8', models.CharField(blank=True, db_column='Column_8', max_length=10, null=True)),
                ('column_9', models.CharField(blank=True, db_column='Column_9', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ss_class',
            },
        ),
        migrations.CreateModel(
            name='TIndent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tradename', models.CharField(blank=True, max_length=40, null=True)),
                ('makeprice', models.CharField(blank=True, max_length=40, null=True)),
                ('money', models.CharField(blank=True, max_length=40, null=True)),
                ('bumber', models.CharField(blank=True, max_length=40, null=True)),
                ('indentnumber', models.CharField(blank=True, max_length=40, null=True)),
                ('intime', models.DateTimeField(blank=True, null=True)),
                ('totalprice', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('column_12', models.CharField(blank=True, db_column='Column_12', max_length=10, null=True)),
                ('column_13', models.CharField(blank=True, db_column='Column_13', max_length=10, null=True)),
                ('column_14', models.CharField(blank=True, db_column='Column_14', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_indent',
            },
        ),
        migrations.CreateModel(
            name='TSite',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('addresname', models.CharField(blank=True, max_length=40, null=True)),
                ('directin', models.CharField(blank=True, max_length=40, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=40, null=True)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('mobilephone', models.CharField(blank=True, max_length=40, null=True)),
                ('column_8', models.CharField(blank=True, db_column='Column_8', max_length=10, null=True)),
                ('column_9', models.CharField(blank=True, db_column='Column_9', max_length=10, null=True)),
                ('column_10', models.CharField(blank=True, db_column='Column_10', max_length=10, null=True)),
                ('column_11', models.CharField(blank=True, db_column='Column_11', max_length=10, null=True)),
                ('column_12', models.CharField(blank=True, db_column='Column_12', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_site',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('nickname', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('aass', models.CharField(blank=True, max_length=10, null=True)),
                ('aassa', models.CharField(blank=True, max_length=10, null=True)),
                ('qwe', models.CharField(blank=True, max_length=10, null=True)),
                ('column_8', models.CharField(blank=True, db_column='Column_8', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='TwoClassify',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(blank=True, max_length=40, null=True)),
                ('column_4', models.CharField(blank=True, db_column='Column_4', max_length=10, null=True)),
                ('column_5', models.CharField(blank=True, db_column='Column_5', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'two_classify',
            },
        ),
    ]
