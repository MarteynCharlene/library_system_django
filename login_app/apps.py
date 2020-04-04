from django.apps import AppConfig

class LoginappConfig(AppConfig):
    name = 'login_app'
    
    def ready(self):
        import login_app.signals