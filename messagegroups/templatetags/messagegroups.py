from django import template
register = template.Library()


@register.inclusion_tag('messagegroups.html')
def render_messages(messages):
    grouped = {}
    for m in messages:
        if (m.level, m.tags) in grouped:
            grouped[(m.level, m.tags)].append(m.message)
        else:
            grouped[(m.level, m.tags)] = [m.message]
    return {'messages': grouped}
