## About

This is a simple hits/miss panel for Johnny cache.

## Installation

```bash
pip install git+git://github.com/streeter/johnny-panel.git#egg=johnny_panel
```

## Usage

1. Add `johnny_panel` to your `INSTALLED_APPS` setting (needed for template file):

```python
INSTALLED_APPS = (
    ...
    'johnny_panel',
)
```

2. Add `johnny_panel.panel.JohnnyPanel` to your `DEBUG_TOOLBAR_PANELS` setting:

```python
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'johnny_panel.panel.JohnnyPanel'
)
```