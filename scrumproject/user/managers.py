from django.contrib.auth.models import (BaseUserManager)

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the provided email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None,  **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        user = self._create_user(
            email=email, 
            username=username, 
            password=password, 
            **extra_fields
        )
        user.is_officer = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Set super user to be staff')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Set user as a super user')

        user = self._create_user(
            email,
            password=password,
            username=username,
            **extra_fields
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
