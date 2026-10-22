from django.utils.translation import gettext, gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PLUGIN_LEVEL_EVENT, PluginConfig
except ImportError:
    raise RuntimeError(
        "Please use pretix 2026.7.0 or above to run this plugin!",
    ) from None


class PluginApp(PluginConfig):
    default = True
    name = "pretix_attendance_certificate_neo"
    verbose_name = "Attendance Certificate"

    class PretixPluginMeta:
        name = gettext_lazy("Attendance Certificate")
        author = "et15, Python Italia"
        description = gettext_lazy("Create Attendance Certificates for your attendees")
        visible = True
        version = __version__
        category = "FEATURE"
        compatibility = "pretix>=2026.7.0"
        level = PLUGIN_LEVEL_EVENT
        settings_links = []
        navigation_links = []

    def ready(self):
        from . import signals  # NOQA

    def installed(self, event):
        if not event.attendance_certificate_layouts.exists():
            event.attendance_certificate_layouts.create(
                name=gettext("Default"),
            )
