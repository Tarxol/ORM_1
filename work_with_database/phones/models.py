from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)