from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PLUGIN_LEVEL_EVENT_ORGANIZER_HYBRID, PluginConfig
except ImportError:
    raise RuntimeError(
        "Please use pretix 2026.7.0 or above to run this plugin!",
    ) from None


class PluginApp(PluginConfig):
    default = True
    name = "pretix_attendance_certificate_neo"
    verbose_name = "Pretix Attendance Certificate neo"

    class PretixPluginMeta:
        name = gettext_lazy("Pretix Attendance Certificate neo")
        author = "et15"
        description = gettext_lazy("Attendance certificates for Pretix")
        visible = True
        version = __version__
        category = "FEATURE"
        compatibility = "pretix>=2026.7.0"
        level = PLUGIN_LEVEL_EVENT_ORGANIZER_HYBRID
        settings_links = []
        navigation_links = []

    def ready(self):
        from . import signals  # NOQA
