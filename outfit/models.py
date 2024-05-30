from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    def __iter__(self):
        for outfit in self.outfits.filter(is_visible=True):
            yield outfit

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'Категорія'
    verbose_name_plural = 'Категорії'
    ordering = ['-sort']


class Outfit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='outfits')
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='outfits/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):        return self.name

    class Meta:
        verbose_name = 'Outfit'
        verbose_name_plural = 'Outfits'
        ordering = ['sort']


