from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from Client.views import ClientViewset
from Contract.views import ContractViewset
from Event.views import EventViewset
from Staff.views import StaffViewset

router = routers.SimpleRouter()
router.register("clients", ClientViewset, basename="clients")
router.register("contracts", ContractViewset, basename="contracts")
router.register("staff", StaffViewset, basename="staff")

contract_router = routers.NestedSimpleRouter(router, "contracts", lookup="contracts")
contract_router.register("events", EventViewset, basename="event")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("", include(router.urls)),
    path("", include(contract_router.urls)),
]
