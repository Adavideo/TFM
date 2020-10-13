from django.db import models
from timeline.models import Thread, Topic


class TopicAnnotation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    label = models.BooleanField()
    annotator = models.IntegerField()

    def __str__(self):
        text = "Annotator "+ str(self.annotator)
        text += " - topic "+ self.topic.name + " "+ str(self.label)
        text += " - thread title: "+ self.thread.title
        return text
