import graphene
from swapi.types import HumanType
from swapi.resolvers import resolver_humans, resolver_human

# 1
class Query(graphene.ObjectType):
    # 2
    hello = graphene.String()
    humans = graphene.List(HumanType)
    human = graphene.Field(HumanType, id=graphene.NonNull(graphene.Int))

    # 3
    def resolve_hello(self, info, **kwargs):
        return "world"

    def resolve_humans(self, info):
        return resolver_humans()

    def resolve_human(self, info, id):
        return resolver_human(id=id)


# 4
schema = graphene.Schema(query=Query)
