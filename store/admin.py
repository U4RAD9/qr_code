from django.contrib import admin
from .models.customer import Users
from .models.Coordinator import Coordinator
from .models.Technician import Technician

# Register your models here.

admin.site.register(Users)
admin.site.register(Coordinator)
admin.site.register(Technician)

