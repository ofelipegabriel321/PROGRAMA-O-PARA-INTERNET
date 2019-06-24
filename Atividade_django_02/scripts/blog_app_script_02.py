from blog_app.models import Blog


def run():
    Blog.objects.get(id=1).delete()
