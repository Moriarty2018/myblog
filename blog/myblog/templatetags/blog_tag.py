from myblog.models import Article,Category,Tag
from django import template

register = template.Library()

@register.simple_tag
def get_new_article(num=5):
    return Article.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def new_date():
    return Article.objects.dates('create_time','month',oreder='DESC')

@register.simple_tag
def new_category():
    return Category.objects.all()

@register.simple_tag
def new_tag():
    return Tag.objects.all()

