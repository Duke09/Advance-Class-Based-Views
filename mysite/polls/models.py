from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def question_and_date(self):
        return "{} posted at {}".format(
            self.question_text,
            self.pub_date
        )

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    def add_vote(self):
        self.votes += 1
        self.save()