from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LeadForm
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
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'درخواست شما با موفقیت ثبت شد به زودی با شما از طریق شماره تماس وارد شده ارتباط میگیریم!')
            return redirect('lead')
    else:
        form = LeadForm()

    return render(request, 'pages/lead.html', {'form': form})
