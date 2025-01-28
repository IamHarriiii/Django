from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title