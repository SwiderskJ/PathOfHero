from user_app.models import UserCurrency


def bank(request):
    if not request.user.is_authenticated:
        return {}
    currency = UserCurrency.objects.get(user=request.user)

    return {
        'currency': currency,
    }
