from django import template

from ..utils import get_user_carts
from carts.models import Cart

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return get_user_carts(request)
