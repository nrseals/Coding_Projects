from django.db import models
import re

from django.db.models.fields import related

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be 2 characters or more"
        if len(postData['last_name']) < 2: 
            errors['last_name'] = "Last name must be 2 characters or more"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email"
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email is not unique"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be 8 characters or more"
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        if len(postData['item']) < 3:
            errors['item'] = "A wish must contain at least 3 characters!"
        if len(postData['description']) < 3:
            errors['description'] = "Description must contain at least 3 characters!"
        return errors 

class Wish(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name="wishes_uploaded", on_delete=models.CASCADE)
    granted = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()


