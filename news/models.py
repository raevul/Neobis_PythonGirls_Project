from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField("Images", upload_to="images")
    created_at = models.TimeField("Created at", auto_now_add=True)

    def __str__(self):
        return self.title