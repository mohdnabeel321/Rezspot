from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from .models import Reservation
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservation')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created successfully!')
            login(request, user)  # Automatically log the user in
            return redirect('reservation')  # Redirect to reservation page after signup
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

# Reservation view
@login_required
def reservation(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        number_of_seats = request.POST['seats']
        cuisine = request.POST['cuisine']
        reservation_date = request.POST['date']
        reservation_time = request.POST['time']
        
        # Create reservation
        reservation = Reservation.objects.create(
            user=request.user,  # Associate reservation with the logged-in user
            name=name,
            phone=phone,
            number_of_seats=number_of_seats,
            cuisine=cuisine,
            reservation_date=reservation_date,
            reservation_time=reservation_time
        )
        messages.success(request, 'Your reservation has been made successfully!')
        return redirect('success')  # Redirect to success page after reservation
    return render(request, 'reservation.html')

# Success view
def success(request):
    return render(request, 'success.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

def menu(request):
    return render(request, 'menu.html')

@login_required
def reservation_status(request):
    user_reservations = Reservation.objects.filter(user=request.user)  # Assuming the Reservation model has a user field.
    return render(request, 'status.html', {'reservations': user_reservations})