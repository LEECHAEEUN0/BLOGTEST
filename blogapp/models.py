from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data publisehd')
    body = models.TextField()
    writer = models.CharField(max_length = 20, default='이채은')
    feeling_of_today= models.TextField()

    def __str__(self):
        return self.title
