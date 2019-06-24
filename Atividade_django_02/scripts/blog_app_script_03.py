from blog_app.models import *


def run():
    Entry.objects.create(headline="BIIIRRRLLL", body_text="Só vim dizer Q so montrão Biirrll, flw monstrãos",
                         pub_date='2017-07-03', blog=Blog.objects.get(id=2))
    Entry.objects.create(headline="Esse post vai sumir ja ja e depois voltar", body_text="Só testando galera. BIIRL!!!",
                         pub_date='2017-07-18', blog=Blog.objects.get(id=2))
    Entry.objects.create(headline="Voltei", body_text="Eu roubei os bolos do Felipe agora ele quer me matar KEEKKEK",
                         pub_date='2018-05-03', blog=Blog.objects.get(id=2))

    Entry.objects.create(headline="666 tão sabendo que criei um blog, ne?", body_text="Ne?",
                         pub_date='2018-01-23', blog=Blog.objects.get(id=3))

    Entry.objects.create(headline="Apresentacao", body_text="Iaê mano, blz? Geovanão Narcizaço aqui trazendo informação",
                         pub_date='2018-10-08', blog=Blog.objects.get(id=4))

    Entry.objects.create(headline="Babado Fortissimo", body_text="Felipe furtou 20 reais de Nelson no shopping. MDS!",
                         pub_date='2019-03-04', blog=Blog.objects.get(id=5))

