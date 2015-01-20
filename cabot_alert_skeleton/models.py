from django.db import models
from cabot.cabotapp.alert import AlertPlugin, AlertPluginUserData

class SkeletonAlert(AlertPlugin):
    name = "Skeleton"
    author = "Jonathan Balls"

    def send_alert(self, service, users, duty_officers):
        """Implement your send_alert functionality here."""
        return

class SkeletonAlertUserData(AlertPluginUserData):
    name = "Skeleton Plugin"
    favorite_bone = models.CharField(max_length=50, blank=True)

