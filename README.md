# pretix-attendance-certificate-neo

Plugin for [pretix](https://github.com/pretix/pretix) to create and send the
certificate of attendance to attendees.

This is a fork of
[pythonitalia/pretix-plugin-attendance-certificate](https://github.com/pythonitalia/pretix-plugin-attendance-certificate),
the plugin used by https://pycon.it. It uses its own Python package
(`pretix_attendance_certificate_neo`), so it can be installed next to the
original plugin; data of the original plugin is not taken over.

## Requirements

pretix 2026.7.0 or newer and Python 3.11 or newer.

## Development setup

1. Make sure that you have a working
   [pretix development setup](https://docs.pretix.eu/en/latest/development/setup.html).
2. Clone this repository.
3. Activate the virtual environment you use for pretix development.
4. Execute `pip install -e .` within this directory to register this
   application with pretix's plugin registry.
5. Execute `make` within this directory to compile translations.
6. Restart your local pretix server. You can now use the plugin from this
   repository for your events by enabling it in the 'plugins' tab in the
   settings.

This plugin has CI set up to enforce a few code style rules with
[Ruff](https://docs.astral.sh/ruff/). To check your plugin for rule violations,
run:

    ruff format --check .
    ruff check .

You can auto-fix most of these issues by running:

    ruff format .
    ruff check --fix .

To automatically check for these issues before you commit, you can run
`.install-hooks.sh`.

Commits in this repository follow
[Conventional Commits](https://www.conventionalcommits.org/) and releases are
cut with [Commitizen](https://commitizen-tools.github.io/commitizen/)
(`cz bump`), which updates the version in `pyproject.toml` and
`pretix_attendance_certificate_neo/__init__.py`, writes `CHANGELOG.md` and
creates the matching git tag.

## Quick start without a pretix checkout

To run the tests and the style checks you do not need a full pretix development
setup. With [uv](https://docs.astral.sh/uv/), a few commands create a throwaway
environment that contains the plugin and pretix from its git master branch:

    uv venv
    source .venv/bin/activate
    uv pip install -e . --group dev --group test
    make
    pytest tests
    ruff check .

`make` needs GNU gettext (Debian package `gettext`). To try the plugin in a
running pretix, use the development setup above instead.

## License

Copyright (c) 2022 Python Italia, Copyright (c) 2026 et15

Released under the terms of the MIT License, see `LICENSE`.
