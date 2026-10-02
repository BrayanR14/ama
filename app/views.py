from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import connection

PRODUCTS = [
    {'id': 1, 'title': 'Prism Flow', 'price': '1.2 ETH', 'image': 'https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&q=80&w=400', 'description': 'An exploration of light refraction.'},
    {'id': 2, 'title': 'Cyber Dusk', 'price': '0.9 ETH', 'image': 'https://images.unsplash.com/photo-1549490349-8643362247b5?auto=format&fit=crop&q=80&w=400', 'description': 'The digital horizon at twilight.'},
    {'id': 3, 'title': 'Neon Soul', 'price': '2.5 ETH', 'image': 'https://images.unsplash.com/photo-1550684848-fac1c5b4e853?auto=format&fit=crop&q=80&w=400', 'description': 'The vibrancy of human consciousness.'},
    {'id': 4, 'title': 'Binary Spirit', 'price': '1.8 ETH', 'image': 'https://images.unsplash.com/photo-1557672172-298e090bd0f1?auto=format&fit=crop&q=80&w=400', 'description': 'Where code meets creativity.'},
    {'id': 5, 'title': 'Void Geometry', 'price': '3.1 ETH', 'image': 'https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?auto=format&fit=crop&q=80&w=400', 'description': 'Abstract shapes in the digital ether.'},
    {'id': 6, 'title': 'Digital Pulse', 'price': '0.5 ETH', 'image': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&q=80&w=400', 'description': 'The rhythmic beat of the network.'},
]

def index(request):
    return render(request, 'index.html')

def health(request):
    """Endpoint de salud. Seenode / balanceadores lo usan para saber si el
    contenedor esta vivo. Verifica tambien que la base de datos responda."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
    except Exception as exc:
        return HttpResponse(f"db error: {exc}", status=503, content_type="text/plain")
    return HttpResponse("ok", content_type="text/plain")

def galery(request):
    # Fixed case sensitivity for Vercel deployment (Galery.html)
    return render(request, 'galery.html', {'products': PRODUCTS})

def About(request):
    return render(request, 'About.html')

def product_detail(request, product_id):
    # Find product by id
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return HttpResponse("Product not found", status=404)
    return render(request, 'product_detail.html', {'product': product})

def checkout(request, product_id):
    # Placeholder: el boton "Buy Now" apunta aqui. Reemplazar por la
    # integracion real de pagos mas adelante.
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return HttpResponse("Product not found", status=404)
    return render(request, 'checkout.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #guarda el usuario
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

