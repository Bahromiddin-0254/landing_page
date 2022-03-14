from django import template

register = template.Library()

@register.filter
def get(queryset,value):
    return queryset.get(employee=value)