from django.db import models

from django.utils.text import slugify
# Create your models here.

# category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    subname = models.CharField(max_length=100)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default=1)  # Replace 1 with an appropriate default value

    def __str__(self):
        return self.subname

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title