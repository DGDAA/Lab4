from django.shortcuts import render

tax_rate = 15/100  # 15% tax rate


def home(request):
    """Default view for homepage."""
    return render(request, 'home.html')


def calculate_total(request, number):
    """View to calculate total price after tax."""
    total = float(number) * (1 + tax_rate)
    return render(request, 'total.html', {'number': number, 'total': total})


def tax_rate_view(request):
    """View to display tax rate."""
    return render(request, 'tax_rate.html', {'tax_rate': tax_rate*100})
