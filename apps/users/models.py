from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_student=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_student=is_student
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prefered_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile-images')
    discord_name = models.CharField(max_length=100)
    github_name = models.CharField(max_length=100)
    fb_profile = models.CharField(max_length=100)
    twitter_profile = models.CharField(max_length=100)
    linkedin_profile = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    codepen = models.CharField(max_length=100)

    phone = models.CharField(max_length=50)

    LEVELS = (
        (1, 'Level One'),
        (2, 'Level Two'),
    )

    current_level = models.IntegerField(choices=LEVELS)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
