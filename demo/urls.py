from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet
# from .views import Another

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('another', Another.as_view()),
]