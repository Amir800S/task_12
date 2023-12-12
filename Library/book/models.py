from django.db import models
from author.models import Author

class Book(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    genre = models.CharField(max_length=150, blank=False, null=False)
    author = models.ForeignKey(
        Author, null=False, related_name='books', on_delete=models.CASCADE
    )
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Книжонка {self.title}"
