from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        app_label = "api"

