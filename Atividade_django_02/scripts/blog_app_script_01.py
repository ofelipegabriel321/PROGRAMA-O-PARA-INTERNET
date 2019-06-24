from blog_app.models import Blog


def run():
    Blog.objects.create(name="Blog do Felipe")
    Blog.objects.create(name="Nelson Blogueiro")
    Blog.objects.create(name="Blogueirinho Pazuzu")
    Blog.objects.create(name="Geovane Noticias")
    Blog.objects.create(name="Fofocas e Babados do Luan")
