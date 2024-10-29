from django import template
from items.models import Item

register = template.Library()

@register.inclusion_tag("items/sinppets/status_select.html")
def item_status_select(instance):
    choices = Item.ItemStatus.choices
    return {
        "instance":instance,
        "choices":choices
    }