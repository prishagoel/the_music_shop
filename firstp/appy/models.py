from django.db import models

# Create your models here.
class UserInfo(models.Model):
    Name = models.CharField(max_length = 5000)
    Phoneno = models.CharField(max_length = 5000, primary_key = True)
    Email = models.CharField(max_length = 5000)
    Passwd = models.CharField(max_length = 5000)

class Guitar(models.Model):
    Sno = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 5000)
    Phoneno = models.CharField(max_length = 5000)

class Piano(models.Model):
    Sno = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 5000)
    Phoneno = models.CharField(max_length = 5000)

class Drums(models.Model):
    Sno = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 5000)
    Phoneno = models.CharField(max_length = 5000)

class Violin(models.Model):
    Sno = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 5000)
    Phoneno = models.CharField(max_length = 5000)