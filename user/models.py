from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    '''Создаем метод для создания пользователя'''
    def _create_user(self, email, username, password, **extra_field):
        # проверяем есть ли email
        if not email:
            raise ValueError("Вы не ввели email")

        if not username:
            raise ValueError("Вы не ввели логин")

        # делаем пользоваетеля
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_field
        )        
        # созраняем пароль
        user.set_password(password)
        user.save(using=self._db)
        return user



    #делаем метод для создания обычного пользователя
    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True) 




class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True) 
    username = models.CharField(max_length=50, unique=True, verbose_name='login') 
    email = models.EmailField(max_length=100, unique=True) 
    is_active = models.BooleanField(default=True) # Статус активации
    is_staff = models.BooleanField(default=False) # Статус админа
    
    USERNAME_FIELD = 'email' # Идентификатор для обращения 
    REQUIRED_FIELDS = ['username'] # Список имён полей для Superuser
 
    objects = MyUserManager() # Добавляем методы класса MyUserManager
    
    # Метод для отображения в админ панели
    def __str__(self):
        return self.email