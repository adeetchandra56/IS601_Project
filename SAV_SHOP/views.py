# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cart(request):
    # Retrieve cart data or items from the database or session
    cart_data = {
        'item1': {'name': 'Product 1', 'price': 20},
        'item2': {'name': 'Product 2', 'price': 30},
        # Add more items as needed
    }

    return render(request, 'cart.html', {'cart_data': cart_data})

def checkout(request):
    # Retrieve cart data from the request or session
    cart_data = request.GET.get('cart_data', '{}')
    # Convert the cart data from a string to a dictionary
    cart_data = eval(cart_data)

    # Perform additional logic or calculations as needed

    return render(request, 'checkout.html', {'cart_data': cart_data})
