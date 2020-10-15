from swapi.models import Human


def resolver_humans():
    return Human.objects.all()
