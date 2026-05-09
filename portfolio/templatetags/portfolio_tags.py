
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


@register.filter
def star_rating(rating):
    """
    Convert a numeric rating (1-5) into HTML star icons.
    Filled stars use fas fa-star, empty stars use far fa-star.
    Usage: {{ testimonial.rating|star_rating|safe }}
    """
    try:
        rating = int(rating)
    except (ValueError, TypeError):
        rating = 0

    if rating < 1:
        rating = 0
    if rating > 5:
        rating = 5

    stars = ''
    for i in range(1, 6):
        if i <= rating:
            stars += '<i class="fas fa-star text-warning"></i>'
        else:
            stars += '<i class="far fa-star text-warning"></i>'
    return stars


@register.filter
def time_ago(value):
    """
    Convert a datetime to a human-readable relative time string.
    Usage: {{ post.published_at|time_ago }}
    """
    from datetime import datetime
    from django.utils import timezone

    if not value:
        return ''

    try:
        if isinstance(value, str):
            value = datetime.fromisoformat(value.replace('Z', '+00:00'))

        now = timezone.now()
        if value.tzinfo is None:
            value = timezone.make_aware(value)

        diff = now - value
        total_seconds = int(diff.total_seconds())

        if total_seconds < 0:
            return 'just now'
        elif total_seconds < 60:
            return 'just now'
        elif total_seconds < 3600:
            minutes = total_seconds // 60
            return f'{minutes} minute{"s" if minutes > 1 else ""} ago'
        elif total_seconds < 86400:
            hours = total_seconds // 3600
            return f'{hours} hour{"s" if hours > 1 else ""} ago'
        elif total_seconds < 604800:
            days = total_seconds // 86400
            return f'{days} day{"s" if days > 1 else ""} ago'
        elif total_seconds < 2592000:
            weeks = total_seconds // 604800
            return f'{weeks} week{"s" if weeks > 1 else ""} ago'
        elif total_seconds < 31536000:
            months = total_seconds // 2592000
            return f'{months} month{"s" if months > 1 else ""} ago'
        else:
            years = total_seconds // 31536000
            return f'{years} year{"s" if years > 1 else ""} ago'
    except Exception:
        return str(value)


@register.filter
def split_by_comma(value):
    """
    Split a comma-separated string into a list for iteration.
    Usage: {% for tag in post.tags|split_by_comma %}
    """
    if not value:
        return []
    return [item.strip() for item in str(value).split(',') if item.strip()]


@register.filter
def format_technology(value):
    """
    Format comma-separated technology string into Bootstrap badges
    Usage: {{ project.technology_used|format_technology|safe }}
    """
    if not value:
        return ''
    
    technologies = [tech.strip() for tech in str(value).split(',') if tech.strip()]
    
    # Technology icon mapping
    tech_icons = {
        'python': 'fab fa-python',
        'django': 'fas fa-code',
        'javascript': 'fab fa-js',
        'js': 'fab fa-js',
        'html': 'fab fa-html5',
        'css': 'fab fa-css3-alt',
        'bootstrap': 'fab fa-bootstrap',
        'react': 'fab fa-react',
        'vue': 'fab fa-vuejs',
        'angular': 'fab fa-angular',
        'node': 'fab fa-node-js',
        'nodejs': 'fab fa-node-js',
        'express': 'fas fa-server',
        'postgresql': 'fas fa-database',
        'postgres': 'fas fa-database',
        'mysql': 'fas fa-database',
        'mongodb': 'fas fa-leaf',
        'redis': 'fas fa-bolt',
        'docker': 'fab fa-docker',
        'kubernetes': 'fab fa-docker',
        'k8s': 'fab fa-docker',
        'git': 'fab fa-git-alt',
        'github': 'fab fa-github',
        'gitlab': 'fab fa-gitlab',
        'aws': 'fab fa-aws',
        'amazon': 'fab fa-aws',
        'linux': 'fab fa-linux',
        'nginx': 'fas fa-server',
        'api': 'fas fa-plug',
        'rest': 'fas fa-exchange-alt',
        'graphql': 'fas fa-project-diagram',
        'jquery': 'fab fa-js',
        'typescript': 'fab fa-js',
        'php': 'fab fa-php',
        'laravel': 'fab fa-laravel',
        'wordpress': 'fab fa-wordpress',
        'flutter': 'fas fa-mobile',
        'android': 'fab fa-android',
        'ios': 'fab fa-apple',
        'swift': 'fab fa-swift',
        'kotlin': 'fab fa-android',
        'java': 'fab fa-java',
        'spring': 'fab fa-java',
        'dotnet': 'fas fa-code',
        'c#': 'fas fa-code',
        'c++': 'fas fa-code',
        'rust': 'fas fa-cogs',
        'go': 'fas fa-code',
        'golang': 'fas fa-code',
        'ruby': 'fab fa-gem',
        'rails': 'fab fa-gem',
    }
    
    badges = []
    for tech in technologies:
        tech_lower = tech.lower().replace(' ', '').replace('-', '').replace('.', '')
        icon_class = None
        
        # Find matching icon
        for key, icon in tech_icons.items():
            if key in tech_lower or tech_lower in key:
                icon_class = icon
                break
        
        # Default icon if no match
        if not icon_class:
            icon_class = 'fas fa-code'
        
        badges.append(f'<span class="badge bg-primary me-1 mb-1" title="{tech}"><i class="{icon_class} me-1"></i>{tech}</span>')
    
    return '\n'.join(badges)


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