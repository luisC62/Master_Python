from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Modelo Vista-Controlador -> Acciones(métodos)
# MVT = Modelo Vista-Template

layout = '''
    <h1>Sitio web con Django | Luis Cárceles &copy 2020</h1>
    <hr/>
    <ul>
        <li><a href="/inicio">Inicio</a></li>
        <li><a href="/hola-mundo">Hola Mundo</a></li>
        <li><a href="/pagina-pruebas">Página de pruebas</a></li>
    </ul>
    <hr/>
'''

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def index(request):
    """
    html = '''
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    '''
    year=2020
    while year <=2050:
        if year % 2 == 0: #Mostrar sólo los años pares
            html += f"<li>{str(year)}</li>"
        year += 1
    html +="</ul>"
    """
    year = 2020
    rango = range(year, 2051)
    nombre = "Luis Cárceles"
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C' ]
    # lenguajes = []
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'year': year,
        'rango': rango
    })

def pagina(request, redirigir=0):
    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ["uno", "dos", "tres"]
    })

def contacto(request, nombre="Luis", apellido="Cárceles"): 
    #Se le pasa los parámetros nombre y apellido a la URL
    #Estos parámetros son opcionales
    #Si se pasan los dos, estos se muestran en la página. Ecc, no se muestra nada
    html = ""
    if nombre and apellido:
        html += "<p>El nombre completo es:</p>"
        html += f" <h3>{nombre} {apellido}</h3>"
    return HttpResponse(layout + html + "<p>&copy 2020</p>")

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title}--->{articulo.content}")

def save_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
    
        return HttpResponse(f"Articulo creado: {articulo.title}--->{articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")

def create_article(request):
    
    return render(request, 'create_article.html')

def create_full_article(request):

    formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })

def articulo(request):
    articulo = Article.objects.get(pk = 3)
    return HttpResponse(f"Articulo: {articulo.id}.{articulo.title}")

def editar_articulo(request, id):
    articulo = Article.objects.get(pk = id)
    articulo.title = "123"
    articulo.content = "Mejor película de Billy Wilder"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo modificado: {articulo.id}.{articulo.title}")

def articulos(request):
    #Petición a la base de datos
    articulos = Article.objects.all().order_by('-id')
    # articulos = Article.objects.filter(
    #     title = "Articulo"
    # ).exclude(public = False)
    # articulos = Article.objects.filter(title = "123")
    # articulos = Article.objects.filter(
    #     Q(title__contains = "2") | Q(title__contains = "Art")
    # )

    #Para consultas SQL:
    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = '123'")

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk = id)
    articulo.delete()
    return redirect('articulos')