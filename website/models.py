from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from stdimage import StdImageField


class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    project_summary = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True)

    image1 = models.ImageField(upload_to='past_projects/%Y/%m/%d',
                               blank=True)

    image2 = models.ImageField(upload_to='past_projects/%Y/%m/%d',
                               blank=True)
    image3 = models.ImageField(upload_to='past_projects/%Y/%m/%d',
                               blank=True)
    image4 = models.ImageField(upload_to='past_projects/%Y/%m/%d',
                               blank=True)
    description = RichTextField(blank=True)
    client_name = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_single',
                       args=[self.id, self.slug])


class Tree(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    scientific_name = models.CharField(max_length=200, blank=True, default='')
    benefits = RichTextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    list_image = StdImageField(upload_to='trees/%Y/%m/%d', blank=True, variations={
        'medium': {"width": 200, "height": 200, "crop": True}
    })
    image1 = models.ImageField(upload_to='trees/%Y/%m/%d',
                               blank=True)
    image2 = models.ImageField(upload_to='trees/%Y/%m/%d',
                               blank=True)
    image3 = models.ImageField(upload_to='trees/%Y/%m/%d',
                               blank=True)
    image4 = models.ImageField(upload_to='trees/%Y/%m/%d',
                               blank=True)
    description = RichTextField(blank=True)
    care = RichTextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tree_single',
                       args=[self.id, self.slug])
