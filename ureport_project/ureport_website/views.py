from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView

from poll.models import Poll

from .models import Partners, Quotes, Read, Watch


def get_read_list():
    return Read.objects.filter(published=True)


def get_quote_list():
    return Quotes.objects.filter(published=True)


class SiteIndexView(TemplateView):
    template_name = 'ureport_website/index.html'

    def get_context_data(self, **kwargs):
        try:
            watchLatest = Watch.objects.latest('id')
        except Watch.DoesNotExist:
            watchLatest = None

        params = {
            'readList': get_read_list(),
            'watchLatest': watchLatest
        }
        return params


class EngageView(TemplateView):
    template_name = 'ureport_website/engage.html'


class NationalPulseView(TemplateView):
    template_name = 'ureport_website/national_pulse.html'


class AboutView(TemplateView):
    template_name = 'ureport_website/about.html'

    def get_context_data(self, **kwargs):
        context = {
            'quoteList': get_quote_list()
        }
        return context


class PollsListView(ListView):
    model = Poll
    template_name = 'ureport_website/polls_list.html'


class PollDetailView(DetailView):
    model = Poll


class PartnersListView(ListView):
    model = Partners
    context_object_name = 'partnersList'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PartnersListView, self).get_context_data(**kwargs)
        context['quoteList'] = get_quote_list()
        return context


class PartnersDetailView(DetailView):
    model = Partners
    context_object_name = 'partnerDetails'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PartnersDetailView, self).get_context_data(**kwargs)
        context['quoteList'] = get_quote_list()
        context['partnersList'] = Partners.objects.filter(published=True)
        return context


class ReadListView(ListView):
    model = Read
    context_object_name = 'readList'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReadListView, self).get_context_data(**kwargs)
        context['quoteList'] = get_quote_list()

        try:
            readLatest = Read.objects.latest('id')
        except Read.DoesNotExist:
            readLatest = None
        context['readLatest'] = readLatest
        return context


class ReadDetailView(DetailView):
    model = Read
    context_object_name = 'readDetails'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PartnersDetailView, self).get_context_data(**kwargs)
        context['quoteList'] = get_quote_list()
        context['readList'] = Read.objects.filter(published=True)
        return context


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
