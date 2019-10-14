from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_proprietor = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class trip(models.Model):
    distance = models.CharField(max_length=255)
    time = models.CharField(max_length=25)
    amount = models.CharField(max_length=9)


class proprietor(models.Model):
    proprietor = models.ForeignKey(User, on_delete=models.CASCADE)
    wage = models.CharField(max_length=9)


class patron(models.Model):
    patron = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.CharField(max_length=9)
