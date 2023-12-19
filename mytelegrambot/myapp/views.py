from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .telegram_bot import run_telegram_bot  # Обратите внимание на корректный путь

def run_bot(request):
    run_telegram_bot()
    return HttpResponse("Telegram bot is running.")