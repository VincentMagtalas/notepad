from builtins import super

from django.db import models

# Create your models here.
class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_text = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)


    def __str__(self):
        return self.note_title



