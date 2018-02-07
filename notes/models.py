from django.db import models

# Create your models here.
class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_text = models.TextField()

    def __str__(self):
        return self.note_title