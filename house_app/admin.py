from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class PropertyInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = PropertyImage
    fk_name = "property"
    extra = 1

class CityInline(admin.TabularInline, TranslationInlineModelAdmin):
        model = City
        extra = 1

@admin.register(Region)
class CityAdmin(TranslationAdmin):
        inlines = [CityInline]

        class Media:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }

@admin.register( Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [PropertyInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Review)

