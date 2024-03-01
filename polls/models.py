from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"{self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    chioce_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.chioce_text}"

class MainNews(models.Model):
    title = models.CharField(max_length = 200)
    head_text = models.TextField(max_length = 2000)
    description = models.TextField()
    news_image = models.ImageField(upload_to = "News/head/")
    created_date = models.TimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"