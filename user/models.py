from django.db import models


# Create your models here.
class User(models.Model):
    GENDER_CHOICES = [('F', 'female'), ('M', 'male')]
    first_name = models.CharField('first_name', max_length=100, null=True)
    last_name = models.CharField('last_name', max_length=100, null=True, blank=True)
    username = models.CharField('username', max_length=100, null=False, unique=True)
    profile = models.TextField('profile', max_length=150, null=True, blank=True)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default="F")
    phone_number = models.CharField('phone_number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=50, null=True)
    country = models.CharField('country', max_length=40, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register_date', auto_now_add=True)
    update_date = models.DateTimeField('update_date')

    @property
    def full_name(self):
        return f'{self.first_name}  {self.last_name}'

    def __str__(self):
        return f'{self.username} registered at {self.register_date}'
