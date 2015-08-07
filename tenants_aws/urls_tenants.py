from users.views import UserViewset
from rest_framework import routers
from django.conf.urls import include, url

router = routers.DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    url(r'^', include(router.urls))
]
