from django.apps import AppConfig

from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    default_site = 'art_auth.admin.CustomAdminSite'


class ArtAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'art_auth'
