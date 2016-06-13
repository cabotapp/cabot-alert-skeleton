from cabot.plugins.models import AlertPlugin
from django import forms
from os import environ as env

from logging import getLogger
logger = getLogger(__name__)

class SkeletonAlertUserSettingsForm(forms.Form):
    favorite_bone = forms.CharField(max_length=100)

class SkeletonAlertPlugin(AlertPlugin):
    name = "Skeleton"
    slug = "cabot_alert_skeleton"
    author = "Jonathan Balls"
    version = "0.0.1"
    font_icon = "fa fa-code"

    user_config_form = SkeletonAlertUserSettingsForm

    def send_alert(self, service, users, duty_officers):
        calcium_level = env.get('CALCIUM_LEVEL') 
        message = service.get_status_message()
        for u in users:
            logger.info('{} - This is bad for your {}.'.format(
                message,
                u.cabot_alert_skeleton_settings.favorite_bone))

        return True

