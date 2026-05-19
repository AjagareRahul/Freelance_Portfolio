"""
Custom Context Processors for Rahul Portfolio Website
"""

from portfolio.models import SiteInfo, SocialLink, Skill, Project


def site_info(request):
    try:
        site_info = SiteInfo.objects.first()
    except Exception:
        site_info = None
    return {'site_info': site_info}


def social_links(request):
    try:
        social_links = SocialLink.objects.filter(is_active=True)
    except Exception:
        social_links = SocialLink.objects.none()
    return {'social_links': social_links}


def visitor_count(request):
    try:
        from portfolio.models import VisitorCount
        visitor, _ = VisitorCount.objects.get_or_create(id=1, defaults={'count': 0})
        visitor_count = visitor.count
    except Exception:
        visitor_count = 0
    return {'visitor_count': visitor_count}


def featured_skills(request):
    try:
        skills = Skill.objects.filter(is_active=True).order_by('-proficiency')[:6]
    except Exception:
        skills = Skill.objects.none()
    return {'featured_skills': skills}


def recent_projects(request):
    try:
        projects = Project.objects.filter(is_published=True).order_by('-created_at')[:3]
    except Exception:
        projects = Project.objects.none()
    return {'recent_projects': projects}
