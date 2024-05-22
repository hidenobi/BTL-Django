from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class SearchTerm(models.Model):
    id = models.IntegerField(primary_key=True)
    q = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.q