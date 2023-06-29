from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    passwd = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    hobby = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id},{self.name},{self.passwd},{self.gender},{self.hobby},{self.job},{self.reg_date}'