from django.contrib import admin

# Register your models here.
from .models import RoomReservation
from .models import Rooms, RoomFacilities, RoomImage

admin.site.register(RoomReservation)
admin.site.register(Rooms)
admin.site.register(RoomFacilities)
admin.site.register(RoomImage)
