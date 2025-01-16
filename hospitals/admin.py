from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(WardBoy)
admin.site.register(Appointment)
admin.site.register(Contact)
