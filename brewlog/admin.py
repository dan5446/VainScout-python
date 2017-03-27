from django.contrib import admin
from actstream import action
import brewlog.models as bl
import reversion

class StreamTrackingAdmin(reversion.VersionAdmin):
    def save_model(self, request, obj, form, change):
        verb = 'Changed' if change else 'Added'
        super(StreamTrackingAdmin, self).save_model(request, obj, form, change)
        action.send(request.user, verb=verb, target=obj)

    def delete_model(self, request, obj):
        action.send(request.user, verb='Deleted', target=obj)
        super(StreamTrackingAdmin, self).delete_model(request, obj)


admin.site.register(bl.Ingredient, StreamTrackingAdmin)
admin.site.register(bl.Hop, StreamTrackingAdmin)
admin.site.register(bl.Grain, StreamTrackingAdmin)
admin.site.register(bl.Recipe, StreamTrackingAdmin)
admin.site.register(bl.Additive, StreamTrackingAdmin)


class MashOrderM2MInline(admin.TabularInline):
    model = bl.MashStep
    extra = 1


class MashAdmin(StreamTrackingAdmin):
    inlines = (MashOrderM2MInline, )


admin.site.register(bl.Mash, MashAdmin)
admin.site.register(bl.MashRest)


class FermentationM2MInline(admin.TabularInline):
    model = bl.FermentationStep
    extra = 1


class FermAdmin(StreamTrackingAdmin):
    inlines = (FermentationM2MInline, )


admin.site.register(bl.Fermentation, FermAdmin)
admin.site.register(bl.FermentationStage)