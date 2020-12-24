from django.contrib import admin
from .models import Appartments


@admin.register(Appartments)
class AppartmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city', 'phone']
    list_display_links = ['id', 'title', 'city', 'phone']