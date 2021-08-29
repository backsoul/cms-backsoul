from graphene_django import DjangoObjectType
import graphene
from .articles.models import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ("id","title","content")

class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticleType)

    @graphene.resolve_only_args
    def resolve_all_articles(self):
        return Article.objects.all()

schema = graphene.Schema(query=Query)