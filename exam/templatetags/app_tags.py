from django import template
import datetime
register=template.Library()
@register.simple_tag(name="get_date")
def get_date():
    now=datetime.datetime.now()
    return now
@register.filter
def quotes(str):
    str='"'+str+'"'
    return str
