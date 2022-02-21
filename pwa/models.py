from django.db import models

class Airdrop(models.Model):
    title = models.CharField(max_length=250, default="", blank=True)
    sub_desc1 = models.CharField(max_length=250, default="", blank=True)
    terms_desc = models.TextField(default="", blank=True)
    
class Meta(models.Model):
    title = models.CharField(max_length=100, default="", blank=True)
    url = models.CharField(max_length=100, default="", blank=True)
    image = models.FilePathField(path="/img")
    image_alt = models.CharField(max_length=100, default="", blank=True)
    desc = models.TextField(default="", blank=True)
    fb_id = models.CharField(max_length=50, default="", blank=True)
    twitter_id = models.CharField(max_length=50, default="", blank=True)
    twitter_image = models.FilePathField(path="/img")
    twitter_card = models.CharField(max_length=50, default="", blank=True)
    twitter_link = models.CharField(max_length=50, default="", blank=True)
    
class Index(models.Model):
    title = models.CharField(max_length=250, default="", blank=True)
    sub_desc1 = models.CharField(max_length=250, default="", blank=True)
    sub_desc2 = models.CharField(max_length=250, default="", blank=True)
    desc = models.TextField(default="", blank=True)
    why_desc = models.TextField(default="", blank=True)
    
class Airdrop_Meta(models.Model):
    title = models.CharField(max_length=100, default="", blank=True)
    url = models.CharField(max_length=100, default="", blank=True)
    image = models.FilePathField(path="/img")
    image_alt = models.CharField(max_length=100, default="", blank=True)
    desc = models.TextField(default="", blank=True)
    fb_id = models.CharField(max_length=50, default="", blank=True)
    twitter_id = models.CharField(max_length=50, default="", blank=True)
    twitter_image = models.FilePathField(path="/img")
    twitter_card = models.CharField(max_length=50, default="", blank=True)
    twitter_link = models.CharField(max_length=50, default="", blank=True)
    
    
    

    
