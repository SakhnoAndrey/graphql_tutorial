import graphene
from swapi.types import HumanType, Gender
from swapi.resolvers import (
    resolver_humans,
    resolver_human,
    resolver_create_human,
    resolver_update_human,
    resolver_delete_human,
)


class Query(graphene.ObjectType):
    hello = graphene.String()
    humans = graphene.List(HumanType)
    human = graphene.Field(HumanType, id=graphene.NonNull(graphene.Int))

    def resolve_hello(self, info, **kwargs):
        return "world"

    def resolve_humans(self, info):
        return resolver_humans()

    def resolve_human(self, info, id):
        return resolver_human(id=id)


class Mutation(graphene.ObjectType):
    create_human = graphene.Field(
        HumanType,
        id=graphene.NonNull(graphene.Int),
        name=graphene.NonNull(graphene.String),
        gender=graphene.NonNull(Gender),
        birth_year=graphene.NonNull(graphene.String),
        mass=graphene.Int(),
        height=graphene.Int(),
        home_planet=graphene.String(),
    )

    def resolve_create_human(
        self, info, id, name, gender, birth_year, mass, height, home_planet
    ):
        return resolver_create_human(
            id, name, gender, birth_year, mass, height, home_planet
        )

    update_human = graphene.Field(
        HumanType,
        id=graphene.NonNull(graphene.Int),
        name=graphene.NonNull(graphene.String),
        gender=graphene.NonNull(Gender),
        birth_year=graphene.NonNull(graphene.String),
        mass=graphene.Int(),
        height=graphene.Int(),
        home_planet=graphene.String(),
    )

    def resolve_update_human(
        self, info, id, name, gender, birth_year, mass, height, home_planet
    ):
        return resolver_update_human(
            id, name, gender, birth_year, mass, height, home_planet
        )

    delete_human = graphene.Field(
        graphene.NonNull(graphene.String),
        id=graphene.NonNull(graphene.Int),
    )

    def resolve_delete_human(self, info, id):
        resolver_delete_human(id)
        return "Deleted successfully!"


# 4
schema = graphene.Schema(query=Query, mutation=Mutation)
