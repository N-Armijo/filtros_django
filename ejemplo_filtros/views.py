from django.shortcuts import render, redirect

# Create your views here.
def vista_ejemplo(request):
    contexto = {'nombre': 'Ana', 'items': ['Manzana','Pera', 'Naranja']}
    # return render(request, 'ejemplo.html', contexto)
    return render(request, 'ejemplo.html', {'contexto' : contexto})

def saludo(request):
    contexto = {'es_usuario' : True}
    return render(request, 'saludo.html',contexto)

def lista_frutas(request):
    frutas = ['Manzana', 'Platano','Naranja','Fresa']
    #para el render Django espera que el segundo argumento sea un diccionario que represente el contexto que se pasará al template
    return render(request, 'frutas.html', {'frutas' : frutas})

def lista_productos(request):
    productos = {'Manzana' : 1.2, 'Platano': 0.8, 'Naranja' : 1.5}
    return render(request, 'productos.html', {'productos':productos})

def lista_nombres(request):
    nombres = ['Ana','Carlos','Beatriz','Juan']
    return render(request, 'nombres.html',{'nombres' : nombres})