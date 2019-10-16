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
    car_model = models.CharField(null=True, max_length=255)
    liscence_no = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_proprietor = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Proprietor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wage = models.CharField(max_length=9)


class Patron(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fare = models.CharField(max_length=9)


class trip(models.Model):
    distance = models.CharField(max_length=255)
    time = models.CharField(max_length=25)
    amount = models.CharField(max_length=9)
    proprietor = models.ForeignKey(Proprietor, on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
