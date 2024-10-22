from django.shortcuts import render, redirect

# Create your views here.
def vista_ejemplo(request):
    contexto = {'nombre': 'Ana', 'items': ['Manzana','Pera', 'Naranja']}
    # return render(request, 'ejemplo.html', contexto)
    return render(request, 'ejemplo.html', {'contexto' : contexto})

def saludo(request):
    contexto = {'es_usuario' : True}
    return render(request, 'saludo.html',contexto)