from django.contrib import admin
from .models import Masaje
from .models import Masajista
from .models import Reservas


# Register your models here.

admin.site.register(Masaje)
admin.site.register(Masajista)
admin.site.register(Reservas)