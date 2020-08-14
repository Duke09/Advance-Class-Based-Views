from django.urls import path, include
from rest_framework import routers
from rest_framework import urlpatterns
from .views import CustomQuestionView, QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register('question', QuestionViewSet)
router.register('choice', ChoiceViewSet)
router.register('custom_question', CustomQuestionView, basename='poll')

urlpatterns = [
    path('', include(router.urls)),
]