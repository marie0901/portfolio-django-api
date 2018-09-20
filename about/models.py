from django.db import models

class AboutSlideManager(models.Manager):
    def get_queryset(self):
        return super(AboutSlideManager, self).get_queryset().filter(published=True)


class AboutSlide(models.Model):
    image = models.ImageField(upload_to='about')
    title = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)

    # API will not serve the slider unless published is set to True
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    visible = AboutSlideManager()

    class Meta:
        ordering = ['order', '-created_at', ]

    def __str__(self):
        orderedTitle = "{:d} | {}".format(self.order, self.title)
        return orderedTitle if self.published else orderedTitle + " (draft)"