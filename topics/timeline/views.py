from django.shortcuts import render
from topics_identifier.models import Document

def timeline_view(request):
    template = "timeline.html"
    all_documents = Document.objects.all()
    context = { "documents_list": all_documents}
    return render(request, template, context)
