# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BTable(models.Model):
    b_name = models.CharField(max_length=40, blank=True, null=True)
    author = models.CharField(max_length=40, blank=True, null=True)
    press = models.CharField(max_length=40, blank=True, null=True)
    pricing = models.CharField(max_length=40, blank=True, null=True)
    d_pricing = models.CharField(max_length=40, blank=True, null=True)
    id_cla = models.ForeignKey('TwoClassify', models.DO_NOTHING, db_column='id_cla', blank=True, null=True)
    pic = models.CharField(max_length=100, blank=True, null=True)
    column_9 = models.CharField(db_column='Column_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_10 = models.CharField(db_column='Column_10', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'b_table'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Indenttable(models.Model):
    id = models.IntegerField(primary_key=True)
    indentid = models.ForeignKey('TIndent', models.DO_NOTHING, db_column='indentid', blank=True, null=True)
    number = models.CharField(max_length=40, blank=True, null=True)
    money = models.CharField(max_length=40, blank=True, null=True)
    bookid = models.ForeignKey(BTable, models.DO_NOTHING, db_column='bookid', blank=True, null=True)
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_9 = models.CharField(db_column='Column_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_10 = models.CharField(db_column='Column_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_11 = models.CharField(db_column='Column_11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_12 = models.CharField(db_column='Column_12', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'indenttable'


class MessBook(models.Model):
    putime = models.DateTimeField(blank=True, null=True)
    edition = models.CharField(max_length=40, blank=True, null=True)
    pritime = models.DateTimeField(blank=True, null=True)
    isbn = models.CharField(max_length=40, blank=True, null=True)
    number = models.CharField(max_length=40, blank=True, null=True)
    pagiation = models.CharField(max_length=40, blank=True, null=True)
    format = models.CharField(max_length=40, blank=True, null=True)
    paper = models.CharField(max_length=40, blank=True, null=True)
    pack = models.CharField(max_length=40, blank=True, null=True)
    impression = models.CharField(max_length=40, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    suit = models.CharField(max_length=40, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    idbook = models.ForeignKey(BTable, models.DO_NOTHING, db_column='idbook', blank=True, null=True)
    column_16 = models.CharField(db_column='Column_16', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_17 = models.CharField(db_column='Column_17', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mess_book'


class OneClassify(models.Model):
    z_name = models.CharField(max_length=40, blank=True, null=True)
    column_3 = models.CharField(db_column='Column_3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_4 = models.CharField(db_column='Column_4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_5 = models.CharField(db_column='Column_5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_6 = models.CharField(db_column='Column_6', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'one_classify'


class SsClass(models.Model):
    one_head = models.CharField(max_length=40, blank=True, null=True)
    two_head = models.CharField(max_length=40, blank=True, null=True)
    column_4 = models.CharField(db_column='Column_4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    one = models.ForeignKey(OneClassify, models.DO_NOTHING, blank=True, null=True)
    two = models.ForeignKey('TwoClassify', models.DO_NOTHING, blank=True, null=True)
    column_7 = models.CharField(db_column='Column_7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_9 = models.CharField(db_column='Column_9', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ss_class'


class TIndent(models.Model):
    tradename = models.CharField(max_length=40, blank=True, null=True)
    makeprice = models.CharField(max_length=40, blank=True, null=True)
    money = models.CharField(max_length=40, blank=True, null=True)
    bumber = models.CharField(max_length=40, blank=True, null=True)
    id_user = models.ForeignKey('TUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    indentnumber = models.CharField(max_length=40, blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    totalprice = models.CharField(max_length=40, blank=True, null=True)
    siteid = models.ForeignKey('TSite', models.DO_NOTHING, db_column='siteid', blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    column_12 = models.CharField(db_column='Column_12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    column_13 = models.CharField(db_column='Column_13', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_14 = models.CharField(db_column='Column_14', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_indent'


class TSite(models.Model):
    addresname = models.CharField(max_length=40, blank=True, null=True)
    directin = models.CharField(max_length=40, blank=True, null=True)
    zipcode = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    mobilephone = models.CharField(max_length=40, blank=True, null=True)
    id_user = models.ForeignKey('TUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_9 = models.CharField(db_column='Column_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_10 = models.CharField(db_column='Column_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_11 = models.CharField(db_column='Column_11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_12 = models.CharField(db_column='Column_12', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_site'


class TUser(models.Model):
    email = models.CharField(max_length=40, blank=True, null=True)
    nickname = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    aass = models.CharField(max_length=10, blank=True, null=True)
    aassa = models.CharField(max_length=10, blank=True, null=True)
    qwe = models.CharField(max_length=10, blank=True, null=True)
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'


class TwoClassify(models.Model):
    s_name = models.CharField(max_length=40, blank=True, null=True)
    id_classify = models.ForeignKey(OneClassify, models.DO_NOTHING, db_column='id_classify', blank=True, null=True)
    column_4 = models.CharField(db_column='Column_4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    column_5 = models.CharField(db_column='Column_5', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'two_classify'
