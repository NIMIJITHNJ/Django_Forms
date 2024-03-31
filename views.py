from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def Product_Review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Review_Confirmation')
    else:
        form = ReviewForm()
    return render(request, 'Product_Review.html', {'form': form})

def Review_Confirmation(request):
    reviews = Review.objects.all()  # Corrected the model name here
    return render(request, 'Review_Confirmation.html', {'reviews': reviews})

def home(request):
    return render(request,"home.html")