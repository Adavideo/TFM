from django.db import models

class Thread(models.Model):
    number = models.IntegerField()
    uri = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)

    def update(self, title, uri):
        self.title = title
        self.uri = uri
        self.save()

    def __str__(self):
        text = "Thread number "+ str(self.number)
        if self.title:
            text += " - title: "+ self.title
        return text
