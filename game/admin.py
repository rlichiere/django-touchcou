
from django.contrib import admin

from . import models


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'participants', 'status', )
    list_filter = ('status', )

    def participants(self, instance):
        return instance.participations.count()


class UserParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'game', 'player_genre', )
    list_filter = ('user', )


admin.site.register(models.Game, GameAdmin)
admin.site.register(models.UserParticipation, UserParticipationAdmin)
