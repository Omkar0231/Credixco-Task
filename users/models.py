from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self,email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a Superuser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email                   = models.EmailField(max_length=254, unique=True)
    password                = models.CharField(max_length=100)
    name                    = models.CharField(max_length=50, null=True)
    father_name             = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth           = models.DateField(null=True)
    gender                  = models.CharField(choices=(("male", "MALE"), ("female", "FEMALE")), default = "", max_length=10)
    password_change_request = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return str(self.email)
