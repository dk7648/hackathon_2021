
import re

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='review', null=True)
    room = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=500, null=True)

    rate_choice = [('5점', '5점'), ('4점', '4점'), ('3점', '3점'), ('2점', '2점'),
                   ('1점', '1점')]
    rate = models.CharField(max_length=10, choices=rate_choice, null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    def summary(self):
        remove_tags = re.compile('<.*?>')
        if len(re.sub(remove_tags, '', self.content)) > 100:
            return re.sub(remove_tags, '', self.content)[:100] + ' ...'
        return re.sub(remove_tags, '', self.content)