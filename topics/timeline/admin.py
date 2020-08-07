from django.contrib import admin
from .models import Thread, Document, Topic, ThreadTopic

admin.site.register(Thread)
admin.site.register(Document)
admin.site.register(Topic)
admin.site.register(ThreadTopic)
