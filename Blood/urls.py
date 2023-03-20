from . import views
from rest_framework_nested import routers
from django.urls import path

main_router = routers.DefaultRouter()

main_router.register('Blood-Request', views.BloodRequestView,
                     basename='blood_request')
main_router.register(
    'Manage-Blood', views.BloodManaging_View, basename='manage_blood')

urlpatterns = main_router.urls
