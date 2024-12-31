from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Return the value of the key in the dictionary."""
    return dictionary.get(key)
