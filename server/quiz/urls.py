from django.urls import path

from .views import QuizPostView, QuestionPostView, GetQuestionView, FinishQuizView, StartQuizView

urlpatterns = [
    path('quiz/', QuizPostView.as_view()),
    path('quiz/<int:pk>/', QuestionPostView.as_view()),
    path('quiz/<int:pk1>/<int:pk2>/', GetQuestionView.as_view()),
    path('quiz/<int:pk>/finish/', FinishQuizView.as_view()),
    path('quiz/<int:pk>/start/', StartQuizView.as_view()),
]