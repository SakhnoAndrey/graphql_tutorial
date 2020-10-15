import graphene


class Gender(graphene.Enum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2
    HERMAPHRODITE = 3


class HumanType(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int)
    name = graphene.NonNull(graphene.String)
    gender = graphene.NonNull(Gender)
    birth_year = graphene.NonNull(graphene.String)
    mass = graphene.Int()
    height = graphene.Int()
    home_planet = graphene.String()
