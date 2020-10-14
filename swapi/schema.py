import graphene

# 1
class Query(graphene.ObjectType):
    # 2
    hello = graphene.String()
    # 3
    def resolve_hello(self, info, **kwargs):
        return "world"


# 4
schema = graphene.Schema(query=Query)
