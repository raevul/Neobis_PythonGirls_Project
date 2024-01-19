from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Girls(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    image = models.ImageField("Images", upload_to="images")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    category = models.ManyToManyField(Category, related_name='category')

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Girl'
        verbose_name_plural = 'Girls'

    def __str__(self):
        return self.name
