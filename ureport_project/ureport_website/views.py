from django.shortcuts import render, get_object_or_404
from .models import Partners, Quotes, Read, Watch


def index(request):
# get the latest Read and Watch posts that are published
    readList = Read.objects.filter(published=True)
    try:
        watchLatest = Watch.objects.latest('id')
    except Watch.DoesNotExist:
        watchLatest = None
    # now return the rendered template
    return render(request, 'index.html', {'readList': readList, 'watchLatest': watchLatest})


def about(request):
# get the quote posts that are published
    quoteList = Quotes.objects.filter(published=True)
    return render(request, 'about.html', {'quoteList': quoteList})


def partners(request):
# get the partners and quote posts that are published
    partnersList = Partners.objects.filter(published=True)
    quoteList = Quotes.objects.filter(published=True)
    return render(request, 'partners.html', {'partnersList': partnersList, 'quoteList': quoteList})


def partnersDetail(request, slug):
# get the partner object and quote posts
    partnersList = Partners.objects.filter(published=True)
    quoteList = Quotes.objects.filter(published=True)
    partnerDetails = get_object_or_404(Partners, slug=slug)
# now return the rendered template
    return render(request, 'partners_detail.html', {'partnersList': partnersList, 'partnerDetails': partnerDetails, 'quoteList': quoteList})


def readArticles(request):
# get the read and quote posts that are published
    readList = Read.objects.filter(published=True)
    quoteList = Quotes.objects.filter(published=True)
    try:
        readLatest = Read.objects.latest('id')
    except Read.DoesNotExist:
        readLatest = None
    return render(request, 'read.html', {'readList': readList, 'readLatest': readLatest, 'quoteList': quoteList})


def readDetail(request, slug):
# get the read  object and quote posts
    readList = Read.objects.filter(published=True)
    quoteList = Quotes.objects.filter(published=True)
    readDetails = get_object_or_404(Read, slug=slug)
# now return the rendered template
    return render(request, 'read_detail.html', {'readList': readList, 'readDetails': readDetails, 'quoteList': quoteList})


def watch(request):
# get the watch and quote posts that are published
    watch = Watch.objects.filter(published=True)
    quoteList = Quotes.objects.filter(published=True)
    try:
        watchLatest = Watch.objects.latest('id')
    except Watch.DoesNotExist:
        watchLatest = None
    return render(request, 'watch.html', {'watchList': watch, 'watchLatest': watchLatest, 'quoteList': quoteList})


def watchDetail(request, slug):
# get the watch object and quote posts
    watch = Watch.objects.filter(published=True)
    quoteList = Quotes.objects.filter(published=True)
    watchDetails = get_object_or_404(Watch, slug=slug)
# now return the rendered template
    return render(request, 'watch_detail.html', {'watchList': watch, 'watchDetails': watchDetails, 'quoteList': quoteList})
