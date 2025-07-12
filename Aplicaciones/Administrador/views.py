from django.shortcuts import render,redirect


# Create your views here.
def admin_panel(request):
    if 'admin_id' not in request.session:
        return redirect('iniciosesion')
    return render(request, 'admin.html')