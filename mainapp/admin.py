from django.contrib import admin
from .models import File
from .models import ArtLine, Home

admin.site.register(File)
admin.site.register(ArtLine)
admin.site.register(Home)

