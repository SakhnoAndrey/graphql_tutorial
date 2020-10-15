from swapi.models import Human


def resolver_humans():
    return Human.objects.all()


def resolver_human(id):
    return Human.objects.get(id=id)
