from django.contrib import admin
from .models import UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)

# superuser info
# username: admin
# password: testpassword
# email: admin@email.com