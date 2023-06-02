from django.urls import path
from . import views


from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),

    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros2', views.libros2, name='libros2'),
    path('libros3', views.libros3, name='libros3'),
    path('libros4', views.libros4, name='libros4'),
    path('libros5', views.libros5, name='libros5'),
    path('libros6', views.libros6, name='libros6'),
    #TABLA01
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('libros/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('descargar_archivo/<int:id>/', views.descargar_archivo, name='descargar_archivo'),
    #TABLA02
    path('libros2/crear2', views.crear2, name='crear2'),
    path('libros2/editar2', views.editar2, name='editar2'),
    path('libros2/eliminar2/<int:id>', views.eliminar2, name='eliminar2'),
    path('libros2/editar2/<int:id>', views.editar2, name='editar2'),
    path('descargar_archivo2/<int:id>/', views.descargar_archivo2, name='descargar_archivo2'),
        #TABLA03
    path('libros3/crear3', views.crear3, name='crear3'),
    path('libros3/editar3', views.editar3, name='editar3'),
    path('libros3/eliminar3/<int:id>', views.eliminar3, name='eliminar3'),
    path('libros3/editar3/<int:id>', views.editar3, name='editar3'),
    path('descargar_archivo3/<int:id>/', views.descargar_archivo3, name='descargar_archivo3'),
        #TABLA04
    path('libros2/crear4', views.crear4, name='crear4'),
    path('libros2/editar4', views.editar4, name='editar4'),
    path('libros2/eliminar4/<int:id>', views.eliminar4, name='eliminar4'),
    path('libros2/editar4/<int:id>', views.editar4, name='editar4'),
    path('descargar_archivo4/<int:id>/', views.descargar_archivo4, name='descargar_archivo4'),
        #TABLA05
    path('libros2/crear5', views.crear5, name='crear5'),
    path('libros2/editar5', views.editar5, name='editar5'),
    path('libros2/eliminar5/<int:id>', views.eliminar5, name='eliminar5'),
    path('libros2/editar5/<int:id>', views.editar5, name='editar5'),
    path('descargar_archivo5/<int:id>/', views.descargar_archivo5, name='descargar_archivo5'),
        #TABLA06
    path('libros2/crear6', views.crear6, name='crear6'),
    path('libros2/editar6', views.editar6, name='editar6'),
    path('libros2/eliminar6/<int:id>', views.eliminar6, name='eliminar6'),
    path('libros2/editar6/<int:id>', views.editar6, name='editar6'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)