from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# the ready function is created to connect the post_save signal to the users model

    def ready(self):
        import users.signals
