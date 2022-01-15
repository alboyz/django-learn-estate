from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampUUIDModel

User = get_user_model()

# gender_option = (
# ("MALE", _("MALE")),
# ("FEMALE", _("FEMALE"))
# )


class Gender(models.TextChoices):
    MALE = "MALE", _("MALE")
    FEMALE = "FEMALE", _("FEMALE")


class Profile(TimeStampUUIDModel):
    user = models.OneToOneField(User,
                                related_name='profile',
                                on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_('phone number'),
                                    max_length=30)
    about_me = models.TextField(verbose_name=_('about me'),
                                default='Say something about yourself')
    liscence = models.TextField(verbose_name=_('Real Estate Liscence'),
                                max_length=20,
                                blank=True,
                                null=True)
    profile_photo = models.ImageField(verbose_name=_('profile photo'),
                                      default='/profile_default.png')
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default="MALE",
        max_length=20,
    )
    country = CountryField(verbose_name=_('country'),
                           default='INA',
                           blank=False,
                           null=False)
    city = models.CharField(verbose_name=_('city'),
                            max_length=180,
                            default='Jakarta',
                            blank=False,
                            null=False)
    is_seller = models.BooleanField(
        verbose_name=_('Seller'),
        default=False,
        help_text=_('Are You looking to buy property'),
    )
    is_buyer = models.BooleanField(
        verbose_name=_('Buyer'),
        default=False,
        help_text=_('Are You looking to sell property'),
    )
    is_agent = models.BooleanField(
        verbose_name=_('Agent'),
        default=False,
        help_text=_('Are You agent property?'),
    )
    top_agent = models.BooleanField(verbose_name=_('top agent'), default=False)
    rating = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    num_reviews = models.IntegerField(verbose_name=_('numbers of reviews'),
                                      default=0,
                                      null=True,
                                      blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
