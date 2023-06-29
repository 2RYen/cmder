from django.db import models

# Create your models here.
class Post2(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    writer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}] {self.subject}'