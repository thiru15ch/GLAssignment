from django.db import models

class Question(models.Model):    
    question = models.CharField(max_length = 100)

    def __str__(self):
        return self.question
    
class Choice(models.Model):    
    question = models.ForeignKey("Question", related_name="choices", on_delete = models.CASCADE)
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


