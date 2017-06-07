from django.contrib import admin

from .models import PageView
from .models import Sender, Email, Receiver, History

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
admin.site.register (Sender)
admin.site.register (Receiver)
admin.site.register (Email)
admin.site.register (History)