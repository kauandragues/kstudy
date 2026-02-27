from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request=request, template_name="estudos/paginas/home.html", status=200)


def materia(request, id):
    return render(
        request=request, template_name="estudos/paginas/materia-view.html", status=200
    )
