import graphene
from swapi.types import HumanType
from swapi.resolvers import resolver_humans

# 1
class Query(graphene.ObjectType):
    # 2
    hello = graphene.String()
    humans = graphene.List(HumanType)
    # 3
    def resolve_hello(self, info, **kwargs):
        return "world"

    def resolve_humans(selfself, info):
        return resolver_humans()


# 4
schema = graphene.Schema(query=Query)
