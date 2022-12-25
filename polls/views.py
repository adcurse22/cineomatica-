from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .models import Cinema
from django.shortcuts import redirect
from .models import Ticket
from django.shortcuts import render, get_object_or_404
from .models import Ticket, Showtime


def movie_list(request):
    """cписок фильмов"""
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'cinematica/movie_list.html', context)


def movie_detail(request, movie_id):
    """для детальной информации о фильме"""
    movie = Movie.objects.get(id=movie_id)
    context = {'movie': movie}
    return render(request, 'cinematica/movie_detail.html', context)


def book_ticket(request):
    if request.method == 'POST':
        # создаем новый билет
        ticket = Ticket(
            movie_id=request.POST['movie_id'],
            date=request.POST['date'],
            time=request.POST['time'],
            seat=request.POST['seat']
        )
        ticket.save()
        return redirect('cinematica:ticket_confirmation', ticket_id=ticket.id)
    else:
        # отображаем форму бронирования
        context = {}
        return render(request, 'cinematica/book_ticket.html', context)


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'cinemas/cinema_list.html', {'cinemas': cinemas})


def cinema_detail(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    return render(request, 'cinemas/cinema_detail.html', {'cinema': cinema})
