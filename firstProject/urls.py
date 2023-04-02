
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "SG Admin"
admin.site.site_title = "SG Admin Portal"
admin.site.index_title = "Welcome to SG"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include('Home.urls'))
]
