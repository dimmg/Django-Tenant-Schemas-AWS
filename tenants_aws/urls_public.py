from customers.views import CustomerViewset
from rest_framework import routers
from django.conf.urls import include, url

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewset)

urlpatterns = [
    url(r'^', include(router.urls))
]
