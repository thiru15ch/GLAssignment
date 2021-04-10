from .models import Question,Choice
from .serializers import QuestionSerializer,ChoiceSerializer
from rest_framework import viewsets

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceView(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer  