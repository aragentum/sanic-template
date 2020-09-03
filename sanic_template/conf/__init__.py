import importlib
import logging
import os

SETTINGS_MODULE_PATH: str = "SANIC_TEMPLATE_SETTINGS_MODULE"


class StandardSetting:
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        settings_module_path = os.environ.get(SETTINGS_MODULE_PATH, "sanic_template.settings.development")
        if not settings_module_path:
            raise Exception("Settings module is not found")

        self._load_settings(settings_module_path)

    def __getattr__(self, name):
        """Return the value from extension settings, cache or module settings."""
        return self.__dict__.get(name)

    def get_config(self) -> dict:
        return self.settings

    def _load_settings(self, settings_module_path: str):
        mod = importlib.import_module(settings_module_path)
        for setting in dir(mod):
            if setting.isupper():
                setattr(self, setting, getattr(mod, setting))


settings = StandardSetting()
