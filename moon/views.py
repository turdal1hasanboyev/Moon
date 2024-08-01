from django.shortcuts import render, redirect

from moon.models import User, SpecialOffers, GetInTouch, Products, AboutMoon


def index(request):
    user = User.objects.get(id=1)
    about_moon = AboutMoon.objects.get(id=1)

    special_offers = SpecialOffers.objects.all().order_by('id')[:3]
    products = Products.objects.all().order_by('id')[:5]

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        GetInTouch.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )

        return redirect('/')

    context = {
        'user': user,
        'special_offers': special_offers,
        'products': products,
        'about_moon': about_moon,
    }
    
    return render(request, 'index.html', context)
