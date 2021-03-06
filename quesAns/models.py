from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.TextField()
    ques_num=models.PositiveIntegerField(default=0,verbose_name='question number')
    answer=models.CharField(max_length=200)
    asset=models.URLField(max_length=500,verbose_name='assets')

    def __str__(self):
        return f'{self.question[:20]}...'