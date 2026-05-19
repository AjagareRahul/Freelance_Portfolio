"""
Custom Middleware for Rahul Portfolio Website
"""

from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.utils import timezone
from portfolio.models import VisitorCount, UserActivity


class VisitorCountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            from portfolio.models import VisitorCount
            visitor_count, _ = VisitorCount.objects.get_or_create(id=1, defaults={'count': 0})
            if request.path == '/' or request.path == '':
                if not request.session.get('visitor_counted', False):
                    visitor_count.count += 1
                    visitor_count.save()
                    request.session['visitor_counted'] = True
            request.visitor_count = visitor_count.count
        except Exception:
            request.visitor_count = 0
        return None


class LastVisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.user.is_authenticated:
                request.session['last_visit'] = str(timezone.now())
                last_visit = request.session.get('last_visit')
                if last_visit:
                    from portfolio.models import UserActivity
                    UserActivity.objects.create(
                        user=request.user,
                        activity_type='visit',
                        description=f'User visited at {timezone.now()}'
                    )
        except Exception:
            pass
        return None

    def process_response(self, request, response):
        if not request.user.is_authenticated:
            if 'last_visit' not in request.COOKIES:
                response.set_cookie('last_visit', str(timezone.now()), max_age=60*60*24*365)
        return response
