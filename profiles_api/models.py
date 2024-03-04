from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Custom user model manager"""
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('An email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password) # Hashes the password
        user.save(using=self._db) # Standard convention
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True # Automatically created by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DB model for users in the app"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    def get_full_name(self):
        """Retrieve the full name for user instance"""
        return self.name

    def get_short_name(self):
        """Retrieve the short name for user instance"""
        return self.name

    def __str__(self):
        """Returns the string representation of the user instance"""
        return self.email
