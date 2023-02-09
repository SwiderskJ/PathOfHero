from hero_app.models import Hero
from user_app.models import UserCurrency


def bank(request):
    if not request.user.is_authenticated:
        return {}
    currency = UserCurrency.objects.get(user=request.user)

    return {
        'currency': currency,
    }


def hero(request):
    if not request.user.is_authenticated:
        return {}
    if request.session.get('actual_hero') is None:
        return {}
    session_hero = request.session['actual_hero']
    session_hero = Hero.objects.get(id=session_hero)
    return {
        'session_hero': session_hero
    }


def user(request):
    if not request.user.is_authenticated:
        return {}

    return {
        'user': request.user,
    }
