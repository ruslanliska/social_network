from django.utils.timezone import now
from .models import Profile


class LastActivityTraceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        member: Profile = request.user
        if member.is_authenticated:
            member.last_login = now()
            member.save()
        return response