
import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.core.management import call_command
from myapp.models import Student

print("Applying migrations (first run only takes a moment)...")
call_command("makemigrations", "myapp", interactive=False, verbosity=0)
call_command("migrate", interactive=False, verbosity=0)

print("Creating student...")
start = time.time()
Student.objects.create(name="Shikhar")  
elapsed = time.time() - start
print(f"Time taken: {elapsed:.2f} seconds")
