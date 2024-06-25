from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, blank=True)  
    last_name = models.CharField(max_length=20, blank=True)  
    is_staff = models.BooleanField(default=False)
    is_active = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    '''
    The USERNAME_FIELD attribute specifies which field on the user model should be used for uniquely identifying a user. 
    By default, Django uses the username field, but since you are creating a custom user model that uses the email address for authentication, you set USERNAME_FIELD to 'email'.
    '''
    REQUIRED_FIELDS = []   
    '''
    The REQUIRED_FIELDS attribute is a list of fields that are required when creating a user via the Django admin 
    or the createsuperuser management command, apart from the USERNAME_FIELD and password which are required by default.
    '''
    
    def __str__(self):
        return self.email 