from django.db import models


class Thread(models.Model):
    number = models.IntegerField()
    uri = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)

    def update(self, title, uri):
        self.title = title
        self.uri = uri
        self.save()

    def news(self):
        news = Document.objects.filter(is_news=True, thread=self)
        if news: return news[0]
        return None

    def comments(self):
        comments = Document.objects.filter(is_news=False, thread=self).order_by("date")
        return comments

    def documents_content(self):
        content = []
        news_content = self.news().content
        content.append(news_content)
        for comment in self.comments():
            content.append(comment.content)
        return content

    def assign_topic(self, topic):
        thread_topic, created = ThreadTopic.objects.get_or_create(thread=self, topic=topic)

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


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_threads(self):
        topic_threads_list = ThreadTopic.objects.filter(topic=self)
        threads = []
        for topic_thread in topic_threads_list:
            threads.append(topic_thread.thread)
        return threads

    def __str__(self):
        return self.name


class ThreadTopic(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        text = str(self.thread)+ " - topic: " + self.topic.name
        return text
