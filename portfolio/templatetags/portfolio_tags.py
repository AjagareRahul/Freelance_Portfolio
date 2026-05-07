
# ==================== Custom Tags ==================== 

from django import template

register = template.Library()


@register.simple_tag
def get_social_icon(platform):
    """
    Get Font Awesome icon class for social platform
    """
    icons = {
        'github': 'fab fa-github',
        'linkedin': 'fab fa-linkedin',
        'twitter': 'fab fa-twitter',
        'x': 'fab fa-x-twitter',
        'instagram': 'fab fa-instagram',
        'facebook': 'fab fa-facebook',
        'youtube': 'fab fa-youtube',
        'stackoverflow': 'fab fa-stack-overflow',
        'medium': 'fab fa-medium',
        'blog': 'fas fa-blog',
    }
    return icons.get(platform, 'fas fa-link')


@register.simple_tag
def get_skill_icon(skill_name):
    """
    Get Font Awesome icon for skill
    """
    skill_icons = {
        'python': 'fab fa-python',
        'django': 'fas fa-code',
        'javascript': 'fab fa-js',
        'html': 'fab fa-html5',
        'css': 'fab fa-css3-alt',
        'react': 'fab fa-react',
        'vue': 'fab fa-vuejs',
        'angular': 'fab fa-angular',
        'node': 'fab fa-node-js',
        'sql': 'fas fa-database',
        'docker': 'fab fa-docker',
        'git': 'fab fa-git-alt',
    }
    
    skill_lower = skill_name.lower()
    for key, icon in skill_icons.items():
        if key in skill_lower:
            return icon
    
    return 'fas fa-code'


@register.simple_tag
def get_upcoming_project_icon(status):
    """
    Get icon for upcoming project based on status
    """
    icons = {
        'planned': 'far fa-calendar-plus',
        'in_development': 'fas fa-code-branch',
        'testing': 'fas fa-vial',
        'launching_soon': 'fas fa-rocket',
    }
    return icons.get(status, 'far fa-calendar')


@register.inclusion_tag('portfolio/tags/skills_progress.html')
def render_skills_progress(skills):
    """
    Render skills with progress bars
    """
    return {'skills': skills}


@register.inclusion_tag('portfolio/tags/project_card.html')
def render_project_card(project):
    """
    Render project card
    """
    return {'project': project}


@register.inclusion_tag('portfolio/tags/testimonial_card.html')
def render_testimonial_card(testimonial):
    """
    Render testimonial card
    """
    return {'testimonial': testimonial}


@register.inclusion_tag('portfolio/tags/message_alert.html')
def show_messages(messages):
    """
    Render Django messages as Bootstrap alerts
    """
    return {'messages': messages}


@register.simple_tag
def get_site_version():
    """
    Get site version
    """
    return '2.1.0'


@register.simple_tag
def get_current_year():
    """
    Get current year
    """
    from django.utils import timezone
    return timezone.now().year


@register.simple_tag
def url_replace(request, field, value):
    """
    Replace URL parameter and return new URL
    """
    from django.utils.http import urlencode
    dict_ = request.GET.copy()
    dict_[field] = value
    return urlencode(dict_)