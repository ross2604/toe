from django.shortcuts import render

from django.core.urlresolvers import reverse

import vanilla


class Start(vanilla.TemplateView):
    @classmethod
    def url_name(cls):
        return 'start'
