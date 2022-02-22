from django.contrib import admin
from core.models import Record, BackgroundJob

class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "species", "weight", "length", "latitude", "longitude", "timestamp")
    search_fields = ("name", "species", "weight", "length", "latitude", "longitude")
    list_display_links = ("id", "name")

class BackgroundJobAdmin(admin.ModelAdmin):
    list_display = ("id", "record_id", "record_name")
    # search_fields = ("name", "species", "weight", "length", "latitude", "longitude")

    def record_id(self, instance):
        return instance.record.id

    record_id.description = "Record ID"

    def record_name(self, instance):
        return instance.record.name

    record_name.description = "Record Name"


admin.site.register(Record, RecordAdmin)
admin.site.register(BackgroundJob, BackgroundJobAdmin)