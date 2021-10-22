from django.apps import AppConfig


class {{ cookiecutter.app_slug.upper() }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ cookiecutter.project_slug}}.{{ cookiecutter.app_slug }}'
