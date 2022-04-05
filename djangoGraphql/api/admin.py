from django.contrib import admin
from .models import Director
from .models import Movie

admin.site.register(Director)
admin.site.register(Movie)
