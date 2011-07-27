from debug_toolbar.panels import DebugPanel
from johnny.signals import qc_hit, qc_miss
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

connected = False
class Collector(object):
    def __init__(self):
        self.hits = []
        self.misses = []
        self.connect()

    def __del__(self):
        self.disconnect()
        if hasattr(object, '__del__'):
            object.__del__(self)

    def disconnect(self):
        qc_hit.disconnect(self.hit)
        qc_miss.disconnect(self.miss)

    def connect(self):
        qc_hit.connect(self.hit)
        qc_miss.connect(self.miss)

    def hit(self, *args, **kwargs):
        self.hits.append(kwargs)

    def miss(self, *args, **kwargs):
        self.misses.append(kwargs)

class JohnnyPanel(DebugPanel):
    name = 'Johnny Stats'
    has_content = True

    def process_request(self, *args, **kwargs):
        self.collector = Collector()

    def nav_title(self):
        return _("Johnny Stats")

    def title(self):
        return _('Johnny Cache Stats')

    def url(self):
        return ''

    def content(self):
        context = self.context.copy()
        context.update({'collector':self.collector,
                   'hits': len(self.collector.hits),
                   'misses': len(self.collector.misses)
                  })
        return render_to_string('johnny_panel/johnny.html', context)

    def nav_subtitle(self):
        return "%d hits, %d misses" % (len(self.collector.hits), len(self.collector.misses))
