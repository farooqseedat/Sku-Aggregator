from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email,
                    password=None,
                    is_active=True,
                    is_staff=False,
                    is_admin=False,
                    last_name="",
                    first_name=""
                ):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("Password is required")
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)  # change user password
        user_obj.last_name = last_name
        user_obj.first_name = first_name
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff_user(
                    self, email,
                    password=None,
                    last_name="",
                    first_name=""
                ):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            last_name=last_name,
            first_name=first_name   
        )
        return user

    def create_superuser(
                    self, email,
                    password=None,
                    last_name="",
                    first_name=""
                ):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            last_name=last_name,
            first_name=first_name,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(('email address'), unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non super
    admin = models.BooleanField(default=False)  # superuser
    first_name = models.CharField(max_length=30, blank=True, null= True)
    last_name = models.CharField(max_length=30, blank=True, null= True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
    
    def __str__(self):
        return "{}".format(self.email)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=5)
