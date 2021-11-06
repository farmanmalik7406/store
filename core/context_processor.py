from core.models import Cart
from django.http.response import HttpResponse

def loadCart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        cartTotal = 0
        for carttemp in cart:
            cartTotal = carttemp.total + cartTotal

        return {'cart': cart,'cartTotal':cartTotal}
    else:
        return {'cart': ''}