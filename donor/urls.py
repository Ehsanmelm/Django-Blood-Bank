from . import views
from rest_framework_nested import routers


main_router = routers.DefaultRouter()
main_router.register('donor', views.DonorView, basename='donors')
main_router.register(
    'Donate-Request', views.DonateRequestView, basename='donate_request')

urlpatterns = main_router.urls
