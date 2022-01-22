from django.db import models

from django.utils.translation import gettext_lazy as _
from realestate.settings.base import AUTH_USER_MODEL

from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile

# rating_option = [
# RATING_1= 1, _('poor'),
# (RATING_2=2, _('Fair')),
# (RATING_3=3, _('Good')),
# (RATING_4=4, _('Very Good')),
# (RATING_5=5, _('Excelent'))
# ]


class Rating(TimeStampedUUIDModel):

    class Range(models.IntegerChoices):

        # STATUS = (
        # (1,  _('Available to borrow')),
        # (2, _('Borrowed by someone')),
        # (3, _('Archived - not available anymore')),
        # )

        RATING_1 = 1, _('poor')
        RATING_2 = 2, _('Fair')
        RATING_3 = 3, _('Good')
        RATING_4 = 4, _('Very Good')
        RATING_5 = 5, _('Excelent')

    rater = models.ForeignKey(AUTH_USER_MODEL,
                              verbose_name=_('User providing the user'),
                              on_delete=models.SET_NULL,
                              null=True)
    agent = models.ForeignKey(
        Profile,
        verbose_name=_('Agent being rated'),
        related_name='agent_review',
        on_delete=models.SET_NULL,
        null=True,
    )

    rating = models.IntegerField(
        verbose_name=_('Rating'),
        choices=Range.choices,
        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good 5=Excelent",
        default=0,
    )
    argument = models.TextField(verbose_name=_('Comment'))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
