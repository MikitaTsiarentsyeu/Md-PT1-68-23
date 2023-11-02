from django.shortcuts import render
from datetime import datetime

# Create your views here.
def test(request):
    now = datetime.now()
    return render(request, 'test.html', {'time':now})