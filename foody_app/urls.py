from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("foody/", include("foody.urls")),
    path("admin/", admin.site.urls),
    path("user/",include("employee_management.urls"))

]