from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import About, Blog, Carousel, Features, Pricing, Team, Testimonial, Service
from .forms import NewsletterForm, ContactForm, CommentForm, BookingForm
from django.views.generic import UpdateView, CreateView,  DeleteView
from django.urls import reverse_lazy
# Create your views here.
class AboutUpdateView(UpdateView):
    model = About
    fields = ('name', 'bio', 'img', 'price', 'price2')
    template_name = 'AboutEdit.html'

class AboutDeleteView(DeleteView):
    model = About
    template_name = 'AboutDelete.html'
    success_url = reverse_lazy('index')

class AboutCreateView(CreateView):
    model =About
    template_name = 'AboutCreateView.html'
    fields = ('name', 'bio', 'img', 'price', 'price2')

def Aboutdetail(request, about):
    about = get_object_or_404(About, slug=about)
    context = {
        'about': about
    }
    return render(request, 'aboutDetailView', context=context)

def index(request):
    blog = Blog.objects.all()
    about = About.objects.all()
    carousel = Carousel.objects.all()
    pricing = Pricing.objects.all()
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    features = Features.objects.all()
    service = Service.objects.all()
    booking = BookingForm(request.POST or None)
    if request.method == "POST" and booking.is_valid():
        booking.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    comment = CommentForm(request.POST or None)
    if request.method == "POST" and comment.is_valid():
        comment.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "blog": blog,
        "about": about,
        "carousel": carousel,
        "pricing": pricing,
        "team": team,
        "testimonial": testimonial,
        "features": features,
        "booking": booking,
        "service": service,
        "newsletter": newsletter,
        "contact": contact,
        "comment": comment
    }
    return render(request, 'index.html', context=context)
def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about.html', context=context)
def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'blog.html', context=context)
def booking(request):
    booking = BookingForm(request.POST or None)
    if request.method == "POST" and booking.is_valid():
        booking.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "booking": booking
    }
    return render(request, 'booking.html', context=context)
def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "contact": contact
    }
    return render(request, 'contact.html', context=context)

def comment(request):
    comment = CommentForm(request.POST or None)
    if request.method == "POST" and comment.is_valid():
        comment.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "comment": comment
    }
    return render(request, 'comment.html', context=context)
def price(request):
    pricing = Pricing.objects.all()
    context = {
        'pricing': pricing
    }
    return render(request, 'price.html', context=context)
def service(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request, 'service.html', context=context)
def single(request):
    features = Features.objects.all()
    context = {
        'features': features
    }
    return render(request, 'single.html', context=context)

def aboutdetail(request, id):
    about = About.objects.get(id=id)
    context = {
        'x': about
    }
    return render(request, 'aboutdetail.html', context=context)

def blogdetail(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'x': blog
    }
    return render(request, 'blogdetail.html', context=context)

def carouseldetail(request, id):
    carousel = Carousel.objects.get(id=id)
    context = {
        'x': carousel
    }
    return render(request, 'carouseldetail.html', context=context)

def featuresdetail(request, id):
    features = Features.objects.get(id=id)
    context = {
        'x': features
    }
    return render(request, 'featuresdetail.html', context=context)


def pricingdetail(request, id):
    pricing = Pricing.objects.get(id=id)
    context = {
        'x': pricing
    }
    return render(request, 'pricingdetail.html', context=context)

def teamdetail(request, id):
    team = Team.objects.get(id=id)
    context = {
        'x': team
    }
    return render(request, 'teamdetail.html', context=context)

def testimonialdetail(request, id):
    testimonial = Testimonial.objects.get(id=id)
    context = {
        'x': testimonial
    }
    return render(request, 'testimonialdetail.html', context=context)


def newsletter(request):
    newsletter =NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>So'rovingiz muvaffaqiyatli amalga oshirildi. Rahmat!")
    context = {
        "newsletter": newsletter
    }
    return render(request, 'newsletter.html', context=context)
def servicedetail(request, id):
    service = Service.objects.get(id=id)
    context = {
        'x': service
    }
    return render(request, 'servicedetail.html', context=context)