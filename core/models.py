
# Django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    Modelo de Category
    Atributos:
        category_id INT PK
        name VARCHAR(255) UNIQUE
        active BOOLEAN
    """

    # * Llave primaria
    category_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length= 255,
                            blank=False,
                            null=False,
                            unique=True)
    active = models.BooleanField(default=True)

    # Metadatos
    class Meta:
        verbose_name_plural = "Categories"


    # Método para representar el objeto
    def __str__(self):
        return self.name


class Item_Category(models.Model):
    """
    Modelo de Item_category
    Atributos:
        item_category_id INT PK
        name VARCHAR(255) UNIQUE
        active BOOLEAN
        category_id INT FK
    """

    # * Llave primaria
    item_category_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length= 255,
                            unique=True)
    active = models.BooleanField(default=True)

    # * Atributos relacionales
    category_id = models.ForeignKey(to=Category,
                                    db_column='category_id',
                                    on_delete = models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Item Category"
        verbose_name_plural = "Items Category"

    # Método para representar el objeto
    def __str__(self):
        return self.name


class Person(models.Model):
    """
    Modelo de Person
    Atributos:
        person_id INT PK
        first_name VARCHAR(255)
        second_name VARCHAR(255)
        first_last_name VARCHAR(255)
        second_last_name VARCHAR(255)
    """

    # * Llave primaria
    person_id = models.AutoField(primary_key=True)

    # * Atributos propios
    first_name = models.CharField(max_length=255,
                                  blank=False,
                                  null=False)
    second_name = models.CharField(max_length=255,
                                    blank=True,
                                    null=True)
    first_last_name = models.CharField(max_length=255,
                                       blank=False,
                                       null=False)
    second_last_name = models.CharField(max_length=255,
                                        blank=True,
                                        null=True)

    # Metadatos
    class Meta:
        verbose_name_plural = "Persons"

    # Método para representar el objeto
    def __str__(self):
        return self.first_name +" "+ self.first_last_name


class Section(models.Model):
    """
    Modelo de Section
    Atributos:
        section_id INT PK
        name VARHCAR(255) UNIQUE
        description VARCHAR(1020)   # issue 103
        university_career_id INT FK
    """

    # * Llave primaria
    section_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length=255,
                            unique=True,
                            blank=False,
                            null=False)
    description = models.CharField(max_length=1020,
                                    blank=True,
                                    null=True)

    # * Atributos relacionales
    university_career_id = models.ForeignKey(to=Item_Category,
                                          db_column='university_career_id',
                                          on_delete=models.PROTECT)
 
    # Metadatos
    class Meta:
        verbose_name_plural = "Sections"

    # Método para representar el objeto
    def __str__(self):
        string = ("Section's name: %s, University Career: %s" %(self.name, self.university_career_id))
        return string

class Person_Section(models.Model):
    """
    Modelo de Person Section
    Atributos:
        person_section_id INT PK
        person_id FK
        section_id FK
    """

    # * Llave primaria
    person_section_id = models.AutoField(primary_key=True)

    # * Atributos propios
    person_id = models.ForeignKey(to=Person,
                                  db_column='person_id',
                                  on_delete=models.PROTECT)

    # * Atributos relacionales
    section_id = models.ForeignKey(to=Section,
                                   db_column='section_id',
                                   on_delete=models.PROTECT)
   
    # Metadatos
    class Meta:
        verbose_name = "Relationship Person Section"
        verbose_name_plural = "Relationships Person Section"

class Role(models.Model):
    """
    Modelo de Role
    Atributos:
        role_id INT PK
        name VARCHAR(255) UNIQUE
    """

    # * Llave primaria
    role_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length=255,
                            unique=True)

    # Metadatos
    class Meta:
        verbose_name_plural = "Roles"

    # Método para representar el objeto
    def __str__(self):
        string = ("Role's name: %s" %(self.name))
        return string

class Person_Role(models.Model):
    """
    Modelo de Person_role
    Atributos:
        person_role_id INT
        university_career_id INT FK
        role_id INT FK
        person_id INT FK
    """

    # * Llave primaria
    person_role_id = models.AutoField(primary_key=True)

    # * Atributos relacionales
    university_career_id = models.ForeignKey(to=Item_Category,
                                             db_column='university_career_id',
                                             on_delete = models.PROTECT,
                                             blank=True,
                                             null=True)
    role_id = models.ForeignKey(to=Role,
                                db_column='role_id',
                                on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person,
                                  db_column='person_id',
                                on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Relationship Person Role"
        verbose_name_plural = "Relationships Person Role"

class Person_Media(models.Model):
    """
    Modelo de Person_media
    Atributos:
        person_media_id INT PK
        path VARHCAR(255)
        item_category_id INT FK
        person_id INT FK
    """

    # * Llave primaria
    person_media_id = models.AutoField(primary_key=True)

    # * Atributos propios
    path = models.CharField(max_length=255)

    # * Atributos relacionales
    item_category_id = models.ForeignKey(to=Item_Category,
                                         db_column='item_category_id',
                                         on_delete=models.PROTECT)
    person_id = models.ForeignKey(to=Person,
                                  db_column='person_id',
                                  on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Person Media"
        verbose_name_plural = "Person Medias"

    # Método para representar el objeto
    def __str__(self):
        string = ("Path: %s" %(self.path))
        return string
    

class Person_Contact(models.Model):
    """
    Modelo de Person_Contact
    Atributos:
        person_contact_id INT
        contact VARCHAR(255)
        contact_type_id INT FK
        person_id INT FK
    """

    # * Llave primaria
    person_contact_id = models.AutoField(primary_key=True)

    # * Atributos propios
    contact = models.CharField(max_length=255,
                               null=False)

    # * Atributos relacionales
    contact_type_id = models.ForeignKey(to=Item_Category,
                                        db_column='contact_type_id',
                                        on_delete=models.PROTECT) #revisar BD
    person_id = models.ForeignKey(to=Person,
                                  db_column='person_id',
                                  on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Person Contact"
        verbose_name_plural = "Person Contacts"

    # Método para representar el objeto
    def __str__(self):
        string = ("Contact: %s" %(self.contact))
        return string
    

class Subject_Matter(models.Model):
    """
    Modelo de Subject_matter
    Atributos:
        subject_matter_id INT
        name VARCHAR(255)
        semester INT
        university_career INT FK
    """

    # * Llave primaria
    subject_matter_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length=255)
    semester = models.IntegerField()

    # * Atributos relacionales
    university_career_id = models.ForeignKey(to=Item_Category,
                                             db_column='university_career_id',
                                             on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Subject Matter"
        verbose_name_plural = "Subject Matters"
    
    # Método para representar el objeto
    def __str__(self):
        string = self.name
        return string

class Requirement(models.Model):
    """
    Modelo de Requirement
    Atributos:
        requirement_id INT
        subject_matter_id INT FK
        subject_matter_requirement_id INT FK
    """

    # * Llave primaria
    requirement_id = models.AutoField(primary_key=True)

    # * Atributos relacionales
    subject_matter_id = models.ForeignKey(to='Subject_Matter',
                                          db_column='subject_matter_id',
                                          on_delete=models.PROTECT,
                                          related_name='subject_matter_id_related_name')
    subject_matter_requirement_id = models.ForeignKey(to='Subject_Matter',
                                                      db_column='subject_matter_requirement_id',
                                                      on_delete=models.PROTECT,
                                                      related_name='subject_matter_requirement_id_related_name')

    # Metadatos
    class Meta:
        verbose_name_plural = "Requirements"

    # Método para representar el objeto
    def __str__(self):
        string = ("'%s' as requirement of '%s'" %(self.subject_matter_requirement_id, self.subject_matter_id))
        return string
    

class Content(models.Model):
    """
    Modelo de Content
    Atributos:
        content_id INT PK
        title VARCHAR(255)
        description VARCHAR(255)
        update_time DATE
        create_time DATE
        content_typ_id INT FK
        academic_period_id INT FK
        university_career_id INT FK
        person_id INT FK                # issue 103
    """

    # * Llave primaria
    content_id = models.AutoField(primary_key=True)

    # * Atributos propios
    title = models.CharField(max_length=255,
                             null=False)
    description = models.CharField(max_length=1020,
                                   null=False)
    update_time = models.DateTimeField(default=timezone.now,
                                       null=False,
                                       blank=False)
    create_time = models.DateTimeField(default=timezone.now,
                                       null=False,
                                       blank=False)

    # * Atributos relacionales
    content_type_id = models.ForeignKey(to='Item_Category',
                                        db_column='contact_type_id',
                                        on_delete=models.PROTECT,
                                        related_name='content_type_id_related_name')
    academic_period_id = models.ForeignKey(to='Item_Category',
                                           db_column='academic_period_id',
                                           on_delete=models.PROTECT,
                                           related_name='academic_period_id_related_name',
                                           blank=True,
                                           null=True)
    university_career_id = models.ForeignKey(to='Item_Category',
                                             db_column='university_career_id',
                                             on_delete=models.PROTECT,
                                             related_name='university_career_id_related_name',
                                             blank=True,
                                             null=True)
    person_id = models.ForeignKey(to="Person",
                                db_column='person_id',
                                help_text="The author of the content",
                                on_delete=models.PROTECT,
                                blank=True,
                                null=True)

    # Metadatos
    class Meta:
        verbose_name_plural = "Contents"

    # Método para representar el modelo
    def __str__(self):
        return self.title


class Content_Media(models.Model):
    """
    Modelo de Content_Media
    Atributos:
        content_media_id INT PK
        path VARHCAR(255)
        item_category_id INT
        content_id INT
    """

    # * Llave primaria
    content_media_id = models.AutoField(primary_key=True)

    # * Atributos propios
    path = models.CharField(max_length=500)

    # * Atributos relacionales
    item_category_id = models.ForeignKey(to=Item_Category,
                                         db_column='item_category_id',
                                         on_delete=models.PROTECT)
    content_id = models.ForeignKey(to=Content,
                                   db_column='content_id',
                                   on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Content Media"
        verbose_name_plural = "Contents Media"
    
    # Método para representar el objeto
    def __str__(self):
        string = ("%s" %(self.path))
        return string
    


class Event(models.Model):
    """
    Modelo de Event
    Atributos
        event_id INT PK
        date DATE
        place VARCHAR(255)
        link_form VARCHAR(255)
        url_info VARCHAR(255)
        content_id INT FK
    """

    # * Llave primaria
    event_id = models.AutoField(primary_key=True)

    # * Atributos propios
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=255, null=False)
    link_form = models.CharField(max_length=255, null=False)
    url_info = models.CharField(max_length=255, null=False)

    # * Atributos relacionales
    content_id = models.ForeignKey(to=Content,
                                   db_column='content_id',
                                   on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name_plural = "Events"

    # Método para representar el objeto
    def __str__(self):
        string = ("Evevent with id: %s" %(self.event_id))
        return string
    

class Menu(models.Model):
    """
    Modelo de Menu
    Atributos:
        menu_id INT PK
        name VARCHAR(255) UNIQUE
        order INT
        item_category_id INT FK
    """

    # * Llave primaria
    menu_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length=255,
                            unique=True,
                            null=False)
    order = models.IntegerField()

    # * Atributos relacionales
    item_category_id = models.ForeignKey(to=Item_Category,
                                         db_column='item_category_id',
                                         on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name_plural = "Menus"

    # Método para representar el objeto
    def __str__(self):
        string = ("Menu's name: %s" %(self.name))
        return string
    

class Group(models.Model):
    """
    Modelo para Group
    Atributos:
        group_id INT
        name VARCHAR(255) UNIQUE
        university_career_id INT FK
    """

    # * Llave primaria
    group_id = models.AutoField(primary_key=True)

    # * Atributos propios
    name = models.CharField(max_length=255,
                            unique=True)

    # * Atributos relacionales
    university_career_id = models.ForeignKey(to=Item_Category,
                                             db_column='university_career_id',
                                             on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name_plural = "Groups"

    # Método para representar el objeto
    def __str__(self):
        string = ("%s" %(self.name))
        return string
    

class Group_Contact(models.Model):
    """
    Modelo para Group_Contact
    Atributos:
        group_contact_id INT PK
        contact VARCHAR(45)
        contact_type_id INT FK
        group_id INT FK
    """

    # * Llave primaria
    group_contact_id = models.AutoField(primary_key=True)

    # * Atributos propios
    contact = models.CharField(max_length=255)

    # * Atributos relacionales
    contact_type_id = models.ForeignKey(to=Item_Category,
                                        db_column='contact_type_id',
                                        on_delete=models.PROTECT)
    group_id = models.ForeignKey(to=Group,
                                 db_column='group_id',
                                 on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Group Contact"
        verbose_name_plural = "Group Contacts"

    # Método para representar el objeto
    def __str__(self):
        string = ("Contact: " %(self.contact))
        return string
    


class Group_Event(models.Model):
    """
    Modelo Group_Event
    Atributos:
        group_event_id INT PK
        event_id INT FK
        group_id INT FK
    """

    # * Llave primaria
    group_event_id = models.AutoField(primary_key=True)

    # * Atributos relacionales
    event_id = models.ForeignKey(to=Event,
                                 db_column='event_id',
                                 on_delete=models.PROTECT)
    group_id = models.ForeignKey(to=Group,
                                 db_column='group_id',
                                 on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name = "Relationship Group Event"
        verbose_name_plural = "Relationships Group Event"


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, person_id, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        person_id = Person.objects.get(person_id=person_id)
        email = self.normalize_email(email)
        user = self.model(username = username, email = email, person_id = person_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, person_id, username, email, password):
        person_id = Person.objects.get(person_id=person_id)
        user = self.model(username = username, email = email, person_id = person_id)
        email = self.normalize_email(email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    update_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(default=timezone.now)
    person_id = models.OneToOneField(to=Person,
                                     db_column='person_id',
                                     on_delete=models.PROTECT)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','person_id']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_staff

    def __str__(self):
        return self.email


# Nuevo modelo según Correciones issue 103
# https://github.com/willyborja95/ApiPaginaWeb/issues/103


class Menu_Item(models.Model):
    """
    Modelo de Menu_Item   (Es remplazo del modelo Menu_Item)
    Atributos:
        menu_item_id INT PK
        url VARCHAR(510)
        name VARCHAR(510) UNIQUE
        order INT
        item_category_id INT FK
    """

    # * Llave primaria
    menu_item_id = models.AutoField(primary_key=True)

    # * Atributos propios
    url = models.URLField(max_length=1020,
                            blank=True,
                            null=True)
    name = models.CharField(max_length=255,
                            unique=True,
                            null=False)
    order = models.IntegerField(blank=True,
                                null=True)

    # * Atributos relacionales
    item_category_id = models.ForeignKey(to=Item_Category,
                                         db_column='item_category_id',
                                         on_delete=models.PROTECT)

    # Metadatos
    class Meta:
        verbose_name_plural = "Menu Items"

    # Método para representar el objeto
    def __str__(self):
        string = ("%s" %(self.name))
        return string
    