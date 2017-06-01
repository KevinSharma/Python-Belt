from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def register(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name cannot be less than 2 letters in length.")

        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Not a valid email')

        if len(postData['password']) < 8:
            errors.append("Password is too short.")

# if valid return true and the user objects.

        if len(errors) == 0:
            hashed_pw = bcrypt.hashed_pw(postData['password'].encode('utf-8'),bcrypt.gensalt())

            u  = User.objects.create(email = postData['email'], password = hashed_pw)

            print u

            user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password=hashed_pw)

            print user

            return [True, user]
# if not valid return false and an array of the errors.
        else:
            return [False, errors]

class User(models.Model):
    first_name = models.Charfield(max_length = 40)
    last_name = models.Charfield(max_length = 40)
    email = models.Charfield(max_length = 255)
    password = models.Charfield(max_length = 40)
    conf_pwd = models.Charfield(max_length = 40)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
