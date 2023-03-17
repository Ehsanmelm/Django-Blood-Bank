from rest_framework_nested import routers
from . import views

main_router = routers.DefaultRouter()

main_router.register('patient', views.PatientViewset, basename='patient')

urlpatterns = main_router.urls
