from django.urls import path
from .views import index, about, blog, booking, contact, price, service, single, aboutdetail, teamdetail, testimonialdetail, blogdetail, pricingdetail, featuresdetail, carouseldetail, servicedetail, AboutUpdateView, AboutDeleteView, AboutCreateView
urlpatterns =[
    path('', index, name='index'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('booking', booking, name='booking'),
    path('contact', contact, name='contact'),
    path('price', price, name='price'),
    path('service', service, name='service'),
    path('single', single, name='single'),
    path('aboutdetail/<slug:courses>/', aboutdetail, name='aboutdetail'),
    path('teamdetail/<int:id>/', teamdetail, name='teamdetail'),
    path('testimonialdetail/<int:id>/', testimonialdetail, name='testimonialdetail'),
    path('blogdetail/<int:id>/', blogdetail, name='blogdetail'),
    path('pricingdetail/<int:id>/', pricingdetail, name='pricingdetail'),
    path('featuresdetail/<int:id>/', featuresdetail, name='featuresdetail'),
    path('carouseldetail/<int:id>/', carouseldetail, name='carouseldetail'),
    path('servicedetail/<int:id>/', servicedetail, name='servicedetail'),
    path('about/edit/<slug>/', AboutUpdateView.as_view(), name='aboutUpdate'),
    path('about/delete/<slug>/', AboutDeleteView.as_view(), name='aboutDelete'),
    path('about/create', AboutCreateView.as_view(), name='aboutCreate'),
]