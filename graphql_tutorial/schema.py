import graphene
import swapi.schema
import users.schema


class Query(users.schema.Query, swapi.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, swapi.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
