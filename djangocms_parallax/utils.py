# -*- coding: utf-8 -*-
import os
import uuid


def generate_filename(instance, filename, location):
    extension = os.path.splitext(filename)[1].lower()

    return os.path.join(location, str(uuid.uuid1()) + extension)


def generate_parallax_image_filename(instance, filename):
    return generate_filename(instance, filename, 'djangocms_parallax')