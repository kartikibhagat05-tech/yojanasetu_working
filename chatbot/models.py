from django.db import models
from schemes.models import Scheme

class UserQuery(models.Model):
    user_id = models.CharField(max_length=50)
    message = models.TextField()
    bot_reply = models.TextField(blank=True, null=True)
    bot_schemes = models.ManyToManyField(Scheme, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.message[:20]}"
