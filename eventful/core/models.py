from django.db import models


# Newsletter model
class Newsletter(models.Model):
    main_topic = models.TextField(max_length=1000)
    topic1 = models.TextField(max_length=1000, null=True, blank=True)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.id)
