from blog_app.models import *


def run():
    Blog.objects.get(id=2).entry_set.add(Entry.objects.get(id=2))
