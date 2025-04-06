from django.shortcuts import render
from .models import RunningShoe
from .forms import ShoeSearchForm

def recommend_shoes(request):
    form = ShoeSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        data = form.cleaned_data
        results = RunningShoe.objects.filter(
            surface=data['surface'],
            foot_strike=data['foot_strike'],
            cushioning=data['cushioning'],
            pronation_support=data['pronation_support']
        )

    return render(request, 'shoes/recommend.html', {'form': form, 'results': results})
