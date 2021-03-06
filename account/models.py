from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyManager(BaseUserManager):
    def create_user(
        self, 
        email, 
        first_name, 
        last_name, 
        password, 
        is_student=False, 
        is_teacher=False,
    ):
        if not email:
            raise ValueError('Email is required')
        if is_student == True and is_teacher == True:
            raise ValueError('User can not be both student and teacher')

        if self.model.__name__ == 'Student':
            is_student = True
        if self.model.__name__ == 'Teacher':
            is_teacher = True

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_student=is_student,
            is_teacher=is_teacher,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255, 
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    objects = MyManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'password',
        'first_name',
        'last_name',
    ]

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Student(MyUser):
    institute = models.ForeignKey(
        'Institute',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    chosen_courses = models.ManyToManyField(
        'Course',
        related_name='students',
        blank=True,
    )

    def __str__(self):
        return super().__str__()


class Teacher(MyUser):
    def __str__(self):
        return super().__str__()


class Institute(models.Model):
    name = models.CharField(max_length=100)
    mandatory_courses = models.ManyToManyField(
        'Course',
        related_name='institutes',
        blank=True,
    )

    def __str__(self):
        return self.name
 

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='courses',
    )

    def __str__(self):
        return self.name
