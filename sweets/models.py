from django.db import models


class Pictures(models.Model):
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.image


class Category(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Scoops(models.Model):
    name = models.CharField(max_length=254)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)
    is_vegetarian = models.BooleanField()
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Scoops"

    def __str__(self):
        return self.name


class Bags(models.Model):
    name = models.CharField(max_length=254)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    is_vegetarian = models.BooleanField()
    weight = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Bags"

    def __str__(self):
        return self.name


class Stickers(models.Model):
    name = models.CharField(max_length=254)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Stickers"

    def __str__(self):
        return self.name
