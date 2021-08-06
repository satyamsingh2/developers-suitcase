from django.apps import AppConfig


class RentalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'happy_homes.rentals'

    def ready(self):
        import happy_homes.rentals.signals
