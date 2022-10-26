from django.shortcuts import render

def halaman(request):
    return render(request, 'community/tiga.html')
