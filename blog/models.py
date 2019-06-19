from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:300]

    def fulltext(self):
        return self.body[::]

    def pub_date_only(self):
        return self.pub_date.strftime('%b %e, %Y')


# Add to the admin
