from django.contrib import admin

# Register your models here.

from ECycling.models import cliente
#admin.site.register(cliente)
@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','direccion')
    #search_fields=('nombre')

from ECycling.models import indumentaria
admin.site.register(indumentaria)
from ECycling.models import venta
admin.site.register(venta)

