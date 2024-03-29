#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import environ
env = environ.Env(DEBUG=(bool, False))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

PROJECT_NAME = env('PROJECT_NAME')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
