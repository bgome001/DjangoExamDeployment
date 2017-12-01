from __future__ import unicode_literals
import bcrypt
from django.db import models

class UserManager(models.Manager):
    def validate_registration(self, post_data):
        print post_data
        errors = []
        if len(post_data["password"]) < 8:
            errors.append('password must be at least 8 characters')
        if post_data['password'] != post_data['confirm password']:
           errors.append('password must be the same as confirm password')
        return errors
    def create_user(self, clean_data):
        hashed = bcrypt.hashpassword(clean_data["password"].encode(). bcrypt.gensalt())
        return self.create(
             password=hashed
        )

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User)
    dob = models.DateField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        managed = True
        db_table = 'fbf_profile'

class Login(models.Model):
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class Create(models.Model):
      name = models.CharField(max_length=255, unique=True)
      alias = models.CharField(max_length=255, unique=True)
      email = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = UserManager()
