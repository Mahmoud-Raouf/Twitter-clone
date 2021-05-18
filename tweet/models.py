from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Tweet(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,blank=True, null=True)
    content = models.CharField(max_length=180)
    image = models.ImageField(upload_to='img_tweet' ,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.content

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.content)
        super(Tweet ,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
