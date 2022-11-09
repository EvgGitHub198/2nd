from django import template
from blog.models import Category

register = template.Library()


#@register.simple_tag()

#def get_categories():
#    return

@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.filter(parent__isnull=True).order_by('name')
    return {'list_category': category}