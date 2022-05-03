from django.db import models


class AbstractPerson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    class Meta():
        abstract = True 

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Student(AbstractPerson):
    institute = models.ForeignKey(
        'Institute',
        on_delete=models.CASCADE,
    )
    chosen_courses = models.ManyToManyField(
        'Course',
        related_name='students',
    )

    def __str__(self):
        return super().__str__()


class Teacher(AbstractPerson):

    def __str__(self):
        return super().__str__()


class Institute(models.Model):
    name = models.CharField(max_length=100)
    mandatory_courses = models.ManyToManyField(
        'Course',
        related_name='institutes',
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
