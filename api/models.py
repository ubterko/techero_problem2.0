from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self,email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        user=self.create_user(email=email, password=password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_proprietor = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class AbstractUser(models.Model):
    name = models.CharField(max_length=30)
    #pic = models.ImageField()
    #phone = models.CharField(max_length=11)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=6)
    city = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Proprietor(AbstractUser):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=30)
    liscnece_no = models.CharField(max_length=15)
    wage = models.CharField(max_length=7, null=True)


class Patron(AbstractUser):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fare = models.CharField(max_length=9, null=True)


class Trip(models.Model):
    distance = models.CharField(max_length=255)
    time = models.CharField(max_length=25)
    amount = models.CharField(max_length=9)
    proprietor = models.ForeignKey(Proprietor, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
