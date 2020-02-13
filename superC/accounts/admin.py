from django.contrib import admin
from accounts.models import User,MessageData, Message

admin.site.register(User)

class MessageDataAdmin(admin.ModelAdmin):
    list_display = ('content',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver', 'message_dataID')

admin.site.register(MessageData, MessageDataAdmin)

admin.site.register(Message, MessageAdmin)
