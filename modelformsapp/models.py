from django.db import models

# Create your models here.

authorchoices= [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=3, choices=authorchoices)
    birthdate = models.DateField(blank=True, null=True)
    bookname = models.CharField(max_length=40)

    def __str__(self):
        return self.name



