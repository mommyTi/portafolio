from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("email")
		abc1 = form_data.get("nombre")
		obj = Registrado.objects.create(email=abc, nombre=abc1)

	context = {
		"el_form": form,
	}
	return render(request,"index.html",context)