from django.db import models


class Post(models.Model):
    image = models.ImageField("image", upload_to="posts-images/")
