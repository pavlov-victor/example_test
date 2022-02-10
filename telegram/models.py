from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=120)
