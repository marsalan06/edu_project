from django.contrib import admin

# Register your models here.
from .models import TeachingSession
# Register your models here.

class TeachingSessionAdmin(admin.ModelAdmin):
    list_display = ['description','teacher', 'student', 'date', 'start_time']
    search_fields = ['teacher__user__username', 'student__user__username']
    list_filter = ['date']
    # raw_id_fields = ['teacher', 'student']
    # autocomplete_fields = ['expertise']
    # readonly_fields = ['end_time']
    class Media:
        # css = {
        #     "all": ["my_styles.css"],
        # }
        js = ["https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.0/jquery.js","admin/js/admin.js"]

admin.site.register(TeachingSession, TeachingSessionAdmin)
