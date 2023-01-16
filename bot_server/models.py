from django.db import models

class Query(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    
    
    def __str__(self) -> str:
        return "Question: "+self.question+" Answer: "+self.answer