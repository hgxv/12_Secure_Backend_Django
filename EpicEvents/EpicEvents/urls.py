from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from CRM.views import ClientViewset, ContractViewset, EventViewset, StaffViewset

router = routers.SimpleRouter()
router.register("clients", ClientViewset, basename="clients")
router.register("contracts", ContractViewset, basename="contracts")
router.register("events", EventViewset, basename="events")
router.register("staff", StaffViewset, basename="staff")

client_router = routers.NestedSimpleRouter(router, "clients", lookup="client")
client_router.register(
    "clients_contracts", ContractViewset, basename="clients_contracts"
)

contract_router = routers.NestedSimpleRouter(
    client_router, "clients_contracts", lookup="clients_contract"
)
contract_router.register("events", EventViewset, basename="events")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("", include(router.urls)),
    path("", include(client_router.urls)),
    path("", include(contract_router.urls)),
]
