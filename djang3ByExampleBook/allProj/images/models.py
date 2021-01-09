from django.db import models
from django.conf import settings

# Create your models here.
from django.utils.text import slugify



class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(db_index=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)
    # many to many relationship, link: https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/.
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, *kwargs)