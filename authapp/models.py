from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')

    def delete(self):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()

