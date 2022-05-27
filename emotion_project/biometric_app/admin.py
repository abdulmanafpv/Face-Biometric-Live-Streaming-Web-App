from django.contrib import admin
from biometric_app.models import Detected,Employee,unreg,Checking
# Register your models here.
admin.site.register(Detected),
admin.site.register(Employee),
admin.site.register(unreg),
admin.site.register(Checking)
