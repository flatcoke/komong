# -*- coding: utf-8 -*-
"""
api.users.models
~~~~~~~~~~~~~~~~
This module implements users basic information.
"""
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager as BaseUserManager)
from django.db import models as m
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        username = self.normalize_email(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,
           PermissionsMixin):
    """
    Users within the Django authentication system are represented by this
    model.
    Email and password are required. Other fields are optional.
    """
    id = m.AutoField(primary_key=True)
    username = m.CharField(_('username'), max_length=30)
    email = m.EmailField(_('email address'), unique=True, max_length=100)
    password = m.CharField(_('password'), max_length=128)
    is_staff = m.BooleanField(_('staff status'), default=False, )
    is_active = m.BooleanField(_('active'), default=True, )
    is_superuser = m.BooleanField(_('superuser'), default=False, )
    last_login_at = m.DateTimeField(_('last login'), blank=True, null=True)
    current_login_at = m.DateTimeField(_('current login'), blank=True,
                                       null=True)
    created_at = m.DateTimeField(_('created_at'), auto_now_add=True,
                                 null=False)
    updated_at = m.DateTimeField(auto_now=True, null=False)
    last_login = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'

        ordering = ['-id']

        indexes = [
            m.Index(fields=['created_at'], name='idx_users_created_at'),
            m.Index(fields=['username'], name='idx_users_username'),
        ]

    def __unicode__(self):
        return self.email

    def is_kmong_email(self):
        try:
            return self.email.split('@')[1] == 'kmong.com'
        except AttributeError:
            return False
