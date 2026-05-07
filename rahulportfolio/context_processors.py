"""
Custom Context Processors for Rahul Portfolio Website
"""

from portfolio.models import SiteInfo, SocialLink, Skill, Project


def site_info(request):
    """
    Context processor to make site information available globally
    """
    site_info = SiteInfo.objects.first()
    return {
        'site_info': site_info,
    }


def social_links(request):
    """
    Context processor to make social links available globally
    """
    social_links = SocialLink.objects.filter(is_active=True)
    return {
        'social_links': social_links,
    }


def visitor_count(request):
    """
    Context processor to make visitor count available globally
    """
    try:
        from portfolio.models import VisitorCount
        visitor = VisitorCount.objects.get(id=1)
        visitor_count = visitor.count
    except (VisitorCount.DoesNotExist, Exception):
        visitor_count = 0
    
    return {
        'visitor_count': visitor_count,
    }


def featured_skills(request):
    """
    Context processor to make featured skills available globally
    """
    skills = Skill.objects.filter(is_active=True).order_by('-proficiency')[:6]
    return {
        'featured_skills': skills,
    }


def recent_projects(request):
    """
    Context processor to make recent projects available globally
    """
    projects = Project.objects.filter(is_published=True).order_by('-created_at')[:3]
    return {
        'recent_projects': projects,
    }
