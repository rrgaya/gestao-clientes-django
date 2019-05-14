from django.contrib import admin
from .models import Venda, ItensDoPedido
from .actions import nfe_emitida, nfe_nao_emitida



class VendaAdmin(admin.ModelAdmin):
    fields = ('numero', 'desconto', 'impostos', 'pessoa', 'valor', 'nfe_emitida')
    readonly_fields =  ('valor',)
    # raw_id_fields = ('pessoa',)
    autocomplete_fields = ["pessoa"]
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('numero', 'id', 'valor', 'nfe_emitida')
    search_fields = ['id', 'pessoa__first_name', 'pessoa__doc__num_doc']
    actions = [nfe_emitida, nfe_nao_emitida]
    # TODO: Refatorar
    # filter_vertical = ('produtos',)
    # filter_horizontal = ('produtos',)


    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
