from django.contrib import admin
from .models import Carousel, About, Features, Pricing, Team, Testimonial, Blog, Booking, Service, Newsletter, Contact, Comment
# Register your models here.
admin.site.register(Carousel)
admin.site.register(Features)
admin.site.register(Pricing)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Comment)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}