from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'reservation_date', 'reservation_time', 'number_of_seats', 'user', 'cuisine', 'created_at', 'updated_at')
    list_filter = ('reservation_date', 'reservation_time', 'user', 'cuisine')
    search_fields = ('name', 'phone', 'user__username', 'cuisine')
    ordering = ('reservation_date', 'reservation_time')

admin.site.register(Reservation, ReservationAdmin)
