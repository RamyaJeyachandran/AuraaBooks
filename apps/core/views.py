from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['user_count'] = User.objects.count()
            context['active_user_count'] = User.objects.filter(is_active=True).count()
            context['staff_count'] = User.objects.filter(is_staff=True).count()
            context['superuser_count'] = User.objects.filter(is_superuser=True).count()
            # Recent users for activity feed
            context['recent_users'] = User.objects.order_by('-date_joined')[:5]
        except Exception:
            context['user_count'] = 0
            context['active_user_count'] = 0
            context['staff_count'] = 0
            context['superuser_count'] = 0
            context['recent_users'] = []

        context['current_user'] = self.request.user
        context['now'] = timezone.now()
        return context
