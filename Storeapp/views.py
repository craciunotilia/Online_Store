from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Product, ShoppingCartItem, CartItem
from django.contrib.auth.decorators import login_required

from .forms import CardDataForm

from django.db.models import Sum
from .forms import ContactForm

from django.views import View


def about_view(request):
    # Logica pentru vizualizarea paginii "About Us"
    return render(request, 'about.html')
def blog_view(request):
    articles = [
        {'title': 'Titlu articol 1', 'content': 'Conținut articol 1'},
        {'title': 'Titlu articol 2', 'content': 'Conținut articol 2'},
        # ... alte articole
    ]
    return render(request, 'blog.html', {'articles': articles})


def storeapp(request):
    html_template = loader.get_template('home/home.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def example_view(request):
    return render(request, 'Storeapp/example.html')


def home(request):
    return render(request, 'Storeapp/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def view_cart(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user)
    return render(request, 'view_cart.html', {'cart_items': cart_items})




@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('some_view')



@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(ShoppingCartItem, pk=item_id, user=request.user)
    item.delete()
    return JsonResponse({'message': 'Product removed from cart successfully.'})
# În Storeapp/views.py
from django.shortcuts import render

class CartView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        return render(request, 'cart.html', {'cart_items': cart_items})




@login_required
def cart_view(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user)
    total = cart_items.aggregate(Sum('product__price'))['product__price__sum']
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def cart(request):
    cart_items = request.session.get('cart', {})
    # Retrieve products from database based on cart_items ids and quantities
    # ...
    return render(request, 'cart.html', {'cart_items': cart_items})




from django.shortcuts import render
from .forms import CardDataForm

def home_view(request):
    # Your code here...
    return render(request, 'home.html')


def card_data_view(request):
    if request.method == 'POST':
        form = CardDataForm(request.POST)
        if form.is_valid():
            form.save()  # Salvează datele cardului în baza de date
            # Poți adăuga logica de procesare a plății aici
            return render(request, 'payment_success.html')  # Afișează pagina de succes
    else:
        form = CardDataForm()

    return render(request, 'card_form.html', {'form': form})  # Afișează formularul de introducere a datelor cardului


def shop_view(request):
    # Logica pentru vizualizarea paginii "Shop"
    return render(request, 'shop.html')


def checkout_view(request):
    return render(request, 'checkout.html')

def order_confirmation_view(request):
    # Logica pentru pagina de confirmare a comenzii
    return render(request, 'order_confirmation.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


