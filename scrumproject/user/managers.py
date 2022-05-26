from django.contrib.auth.models import (BaseUserManager)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username = username,
        )
        user.is_officer = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, is_admin=None, is_active=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username
        )
        user.is_admin = is_admin
        user.is_active = True
        user.save(using=self._db)
        return user
