from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def img_tag(src, width, height, classes="", alt="", is_absolute_src=False, is_lazy=False):
    static_src = static('/modules/' + str(src))
    is_lazy = 'lazy' if is_lazy else 'eager'
    
    if is_absolute_src:
        static_src = src

    html = f'<img src="{static_src}" width="{width}" height="{height}" class="{classes}" alt="{alt}" loading="{is_lazy}" onError="this.src = `https://placehold.co/{width}x{height}`">'
    return mark_safe(html)
