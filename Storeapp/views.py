from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Product, ShoppingCartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CardDataForm



def storeapp(request):
    html_template = loader.get_template('home/home.html')
    context = {}
    return HttpResponse(html_template.render(context, request))


def example_view(request):
    return render(request, 'Storeapp/example.html')


def home(request):
    return render(request, 'home/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def view_cart(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user)
    return render(request, 'view_cart.html', {'cart_items': cart_items})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Verificăm dacă produsul este deja în coșul de cumpărături al utilizatorului
    existing_item = ShoppingCartItem.objects.filter(user=request.user,
                                                    product=product).first()

    if existing_item:
        # Dacă produsul există deja în coș, creștem doar cantitatea
        existing_item.quantity += 1
        existing_item.save()
    else:
        # Dacă produsul nu există în coș, îl adăugăm cu cantitatea 1
        ShoppingCartItem.objects.create(user=request.user, product=product,
                                        quantity=1)

    return JsonResponse({'message': 'Product added to cart successfully.'})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(ShoppingCartItem, pk=item_id, user=request.user)
    item.delete()
    return JsonResponse({'message': 'Product removed from cart successfully.'})
# În Storeapp/views.py
from django.shortcuts import render

def cart_view(request):
    # Logica pentru afișarea coșului de cumpărături
    return render(request, 'cart.html')


def card_data_view(request):
    if request.method == 'POST':
        form = CardDataForm(request.POST)
        if form.is_valid():
            form.save()  # Salvează datele cardului în baza de date
            # Poți adăuga logica de procesare a plății aici
            return render(request, 'payment_success.html')
    else:
        form = CardDataForm()

    return render(request, 'card_form.html', {'form': form})


from django.shortcuts import render
from .forms import CardDataForm


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
