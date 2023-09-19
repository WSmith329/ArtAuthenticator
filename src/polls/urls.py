from django.urls import path

from . import views
from .rest_views import QuestionListCreateView, QuestionRetrieveUpdateDestroyView

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("rest/questions/", QuestionListCreateView.as_view(), name="question-list-create"),
    path("rest/questions/<int:pk>", QuestionRetrieveUpdateDestroyView.as_view(), name="question-retrieve-update-destroy")
]
