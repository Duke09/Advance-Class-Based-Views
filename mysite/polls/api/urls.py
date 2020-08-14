from django.urls import path, include
from rest_framework import routers
from rest_framework import urlpatterns
from .views import QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]