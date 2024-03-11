from django.db import models
from django.contrib.auth import get_user_model
from django_softdelete.models import SoftDeleteModel

# Create your models here.

class Post(SoftDeleteModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
