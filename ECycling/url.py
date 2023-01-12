from django.urls import path
from ECycling.views import crea_clientes,lista_clientes,crea_indumentaria,lista_indumentaria,crea_bicicletas,lista_bicicleta

urlpatterns=[
    path('crea_cliente/',crea_clientes),
    path('lista_clientes/',lista_clientes),
    path('crea_indumentaria/',crea_indumentaria),
    path('lista_indumentaria/',lista_indumentaria),
    path('crea_bicicletas/',crea_bicicletas),
    path('lista_bicicleta/',lista_bicicleta),
 

]