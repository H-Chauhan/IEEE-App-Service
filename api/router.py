from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'sigs', SIGViewSet)
router.register(r'events', EventViewSet)
router.register(r'council', CouncilViewSet)