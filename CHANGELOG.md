## v0.1.16 (2026-08-06)

Last release (0.1.16 on PyPI) of
[pythonitalia/pretix-plugin-attendance-certificate](https://github.com/pythonitalia/pretix-plugin-attendance-certificate),
which this plugin is forked from. Summary of its history from October 2022 to
August 2026, by Marco Acierno / Python Italia:

### Original plugin

- **Feat**: certificate layouts per event, designed in pretix' PDF layout editor, with an empty default layout
- **Feat**: send certificates by email through pretix' bulk sendmail, with email history entries
- **Feat**: log entry texts for certificate emails and layout changes
- **Feat**: buttons to download and send the certificate on each order position
- **Fix**: migration, django.urls import and plugin app config for newer pretix
- **Fix**: log entry display signal, error when no certificate layout exists, HTML of the position buttons
