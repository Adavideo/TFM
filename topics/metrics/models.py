from django.db import models
from timeline.models import Topic, Document


class TopicAnnotation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    label = models.BooleanField()
    annotator = models.IntegerField()

    def __str__(self):
        text = "Annotator "+ str(self.annotator)
        text += " - topic "+ self.topic.name + " "+ str(self.label)
        text += " - document "+ str(self.document.id) + ": "+ self.document.content
        return text
