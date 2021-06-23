from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode

from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            current_site = get_current_site(request)
            subject = 'Cokedama Order Request Confirmation'
            company_email = 'cokedama100@gmail.com'
            message = render_to_string('orders/order/email_template.html', {
                'order': order,
                'cart': cart,
                'domain': current_site.domain,
            })
            order.email_order(subject=subject, message=message, company_email=company_email)
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
