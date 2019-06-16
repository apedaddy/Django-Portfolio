from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length = 250)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add to the admin
