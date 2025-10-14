
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Report, Feed

@receiver(post_save, sender=Report)
def check_report_count(sender, instance, created, **kwargs):
    if created:
        feed = instance.feed
        if feed.reports.count() >= 3:
            feed.is_hidden = True
            feed.save()
