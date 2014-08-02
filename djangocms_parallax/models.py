# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, PlaceholderField

from decimal import Decimal

from djangocms_parallax.utils import generate_parallax_image_filename


class Parallax(CMSPlugin):
    speed = models.DecimalField(max_digits=3,
                                decimal_places=2,
                                default=Decimal('0.2'),
                                help_text=_('Scroll speed ratio of images relative to normal speed.'))
    cover_ratio = models.DecimalField(max_digits=3,
                                      decimal_places=2,
                                      default=Decimal('0.75'),
                                      help_text=_('Percentage of viewport height covered by images.'))
    holder_min_height = models.IntegerField(default=200,
                                            help_text=_('Minimum height of each image holder.'))


class ParallaxImage(CMSPlugin):
    image = models.ImageField(upload_to=generate_parallax_image_filename)
    # mobile_image = models.ImageField(upload_to=generate_parallax_mobile_image_filename)
    extra_height = models.IntegerField(default=0)


class ParallaxContent(CMSPlugin):
    content = PlaceholderField('parallax-content')