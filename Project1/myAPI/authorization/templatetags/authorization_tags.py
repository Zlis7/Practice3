from django import template
from authorization.models import *


register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):

    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


#Не хочу разбираться в таких тегах :(
@register.inclusion_tag('login.html')
def show_categories():
    cats = Category.objects.all()
    return { 'cats': cats }