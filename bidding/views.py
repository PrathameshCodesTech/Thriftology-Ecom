from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import NewArrival, Bid
from .forms import BidForm

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def new_arrivals(request):
    new_arrivals = NewArrival.objects.filter(end_date__gt=timezone.now())
    return render(request, 'new_arrivals.html', {'new_arrivals': new_arrivals})

@login_required
def place_bid(request, new_arrival_id):
    new_arrival = NewArrival.objects.get(id=new_arrival_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.new_arrival = new_arrival
            bid.save()
            return redirect('new_arrivals')
    else:
        form = BidForm()
    return render(request, 'place_bid.html', {'form': form, 'new_arrival': new_arrival})