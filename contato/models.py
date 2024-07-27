from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.email
