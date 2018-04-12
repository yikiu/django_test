from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(BaseItem)
class BaseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(BaseTable)
class BaseTableAdmin(admin.ModelAdmin):
    exclude = ('updated_at', 'created_at')
    list_display = ('id', 'name')
    readonly_fields = ('updated_at', 'created_at')

    def save_model(self, request, obj, form, change):
        fields = [ 'name', ]
        if change:
            obj.save(update_fields=fields)
        else:
            # obj.save()
            from django.db import router
            using=router.db_for_write(obj.__class__, instance=obj)
            meta = obj._meta
            fields = [f for f in meta.local_concrete_fields if f.name in fields]
            update_pk=True
            result=obj._do_insert(meta.base_manager, using=using, fields=fields, update_pk=update_pk, raw=False)
            if update_pk:
                setattr(obj, meta.pk.attname, result)
            obj._state.db = using
            # Once saved, this is no longer a to-be-added instance.
            obj._state.adding = False