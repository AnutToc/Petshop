from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm, CheckoutForm
from .models import Product, Order, OrderItem
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.urls import reverse

class CheckoutView(FormView):
    form_class = CheckoutForm
    template_name = 'cart/checkout.html'
    success_url = reverse_lazy('cart:cart_success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        address = form.cleaned_data['address']
        zip_code = form.cleaned_data['zip_code']
        phone_number = form.cleaned_data['phone_number']
        order_items = self.request.session.get('cart', {})

        order = Order.objects.create(
            user=self.request.user,
            name=name,
            email=email,
            address=address,
            zip_code=zip_code,
            phone_number=phone_number,
        )
        
        total_price = 0
        for product_id, quantity in order_items.items():
            product = Product.objects.get(pk=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price,
                quantity=quantity['quantity']
            )
        
        self.request.session['cart'] = {}
        return super().form_valid(form)

@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    if request.method == 'POST':
        return redirect('cart:cart_checkout')
    cart_items = cart.cart.items()
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_items': cart_items})

@login_required
@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity']
        override = cd.get('override', False)
        if override:
            cart.add(product=product, quantity=quantity, override_quantity=True)
        else:
            cart.add(product=product, quantity=quantity)
    return redirect('/main')

@login_required
def update_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update(product, cd['quantity'])
    return redirect('cart:cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart = Cart(request)
    cart.remove(item_id)
    return redirect('cart:cart_detail')

@login_required
def cart_success(request):
    return render(request, 'cart/cart_success.html')

@login_required
def cart_checkout(request):
    return CheckoutView.as_view()(request)

