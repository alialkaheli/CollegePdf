# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pdf(models.Model):
    book_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    pdf = models.FileField()

    def __str__(self):
        return self.book_name