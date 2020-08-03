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


class Document(models.Model):
    content = models.CharField(max_length=41000, unique=True) # max length news 40921, comments 19996
    is_news = models.BooleanField(null=False)
    date = models.DateTimeField()
    author = models.IntegerField()
    thread = models.ForeignKey(Thread, on_delete=models.SET_NULL, null=True)

    def assign_thread(self, info):
        thread, created = Thread.objects.get_or_create(number=info["thread_number"])
        self.thread = thread
        if self.is_news:
            thread.update(info["title"], info["uri"])
        elif created: thread.save()
        self.save()

    def __str__(self):
        text = "Document "+ str(self.id) + " - "
        if self.is_news: text += "type news, "
        else: text += "type comment, "
        text += "content: "+ self.content
        return text
