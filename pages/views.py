from django.shortcuts import render, redirect
from .forms import Leadform
from .models import Product, Certification


def home(request):
    products = (
        Product.objects
        .prefetch_related("images")
        .order_by("order")[:5]
    )

    return render(request, "pages/home.html", {
        "products": products,
    })



def about(request):
    return render(request, 'pages/about.html')

def certifications(request):
    items = Certification.objects.all()
    return render(request, 'pages/certifications.html', {
        'items': items
    })

def lead(request):
    if request.method == 'POST':
        form = Leadform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead')
    else:
        form = Leadform()

    return render(request, 'pages/lead.html', {'form': form})
