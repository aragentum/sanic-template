import importlib
import os

from loguru import logger

SETTINGS_MODULE_PATH: str = "SANIC_SETTINGS_MODULE"


class StandardSetting:

    def __init__(self) -> None:
        settings_module_path = os.environ.get(SETTINGS_MODULE_PATH, "sanic_template.settings.development")
        if not settings_module_path:
            raise Exception("Settings module is not found")

        self._load_settings(settings_module_path)

    def __getattr__(self, name):
        """Return the value from extension settings, cache or module settings."""
        return self.__dict__.get(name)

    def __setattr__(self, name: str, value) -> None:
        self.__dict__[name] = value

    def get_config(self) -> dict:
        return self.settings

    def _load_settings(self, settings_module_path: str):
        mod = importlib.import_module(settings_module_path)
        for setting in dir(mod):
            if setting.isupper():
                setattr(self, setting, getattr(mod, setting))
        logger.info("Settings from module loaded")


settings = StandardSetting()
