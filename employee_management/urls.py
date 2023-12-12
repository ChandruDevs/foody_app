from django.urls import path

from . import views
app_name = "employee_management"
urlpatterns = [
    path("",views.getallusers,name="getallusers"),
    path("create_user", views.create_user,name="create_user"),
    path('edit/<int:user_id>/',views.edit_user,name ="edit_user"),
    path('edit_team/<int:team_id>/', views.update_team, name="update_team"),
    path("create_team",views.create_team),
    path("delete_team/<int:team_id>/",views.delete_team),
    path("delete_user/<int:user_id>/", views.delete_user),
    path("show_team/<int:team_id>/", views.get_team_details)

]