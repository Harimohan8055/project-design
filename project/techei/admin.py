from django.contrib import admin
from .models import User,City,State,IndividualProfile,InstitutionProfile
# Register your models here.

admin.site.register(User)
admin.site.register(City)
admin.site.register(State)
admin.site.register(IndividualProfile)
admin.site.register(InstitutionProfile)
