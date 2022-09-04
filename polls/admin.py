from django.contrib import admin
from .models import Movie, Feedback, Showtime, Cinema, Room, Seat, HistoryItem, Ticket


admin.site.register(Movie)
admin.site.register(Feedback)
admin.site.register(Showtime)
admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(HistoryItem)
admin.site.register(Ticket)
