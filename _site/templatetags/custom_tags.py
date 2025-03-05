from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def img_tag(src, width, height, classes="", alt=""):
    static_src = static('/modules/' + src)
    html = f'<img src="{static_src}" width="{width}" height="{height}" class="{classes}" alt="{alt}" onError="this.src = `https://placehold.co/{width}x{height}`">'
    return mark_safe(html)
