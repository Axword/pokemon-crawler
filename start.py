#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from manage import main
from apscheduler.schedulers.background import BackgroundScheduler
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from app.tasks import add_new_pokemons, check_data_on_old_pokemons


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(add_new_pokemons, 'interval', minutes=15)
    scheduler.add_job(check_data_on_old_pokemons, 'interval', minutes=15)
    scheduler.start()
    main()
