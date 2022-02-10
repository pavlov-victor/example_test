from django.shortcuts import render

from telegram.services import get_user_from_telegram


def callback_telegram(request):
    user = get_user_from_telegram(request)
