from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.title


class Post_list(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    page_link = models.URLField( unique=True, max_length=500)
    page_name = models.CharField(max_length= 200)

    def __str__(self):
        return self.page_name