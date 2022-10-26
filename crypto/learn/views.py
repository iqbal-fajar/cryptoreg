from django.shortcuts import render

def halaman(request):
    return render(request, 'learn/dua.html')
