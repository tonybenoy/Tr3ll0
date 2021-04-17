from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def _str_(self):
        return self.category_name


class Items(models.Model):
    item = models.CharField(max_length=50)
    itemtitle = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.itemtitle