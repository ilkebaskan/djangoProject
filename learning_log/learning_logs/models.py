from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is interested in."""
    # text ve date_added adında veritabanında 2 sütun oluşturacağız.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the topic."""
        return self.text

class Entry(models.Model):
    """Something spesific learned about a topic."""
    # ForeignKey fieldı "çoktan bire" ilişkiyi temsil eder. Her entry bir Topic ile ilişkilidir.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}..."

