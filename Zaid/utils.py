import sys
import logging
import importlib
from pathlib import Path


def load_plugins(plugin_name):
    """Dynamically load a plugin by name and log the result."""
    logger = logging.getLogger(__name__)
    path = Path(f"Zaid/plugins/{plugin_name}.py")
    name = f"Zaid.plugins.{plugin_name}"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None:
        logger.error("Plugin spec not found for %s", plugin_name)
        return
    module = importlib.util.module_from_spec(spec)
    module.logger = logging.getLogger(plugin_name)
    try:
        spec.loader.exec_module(module)
    except Exception:
        logger.exception("Failed to load plugin %s", plugin_name)
        return
    sys.modules[name] = module
    logger.info("Plugin loaded %s", plugin_name)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Zaid.plugins." + plugin_name] = load
    logging.getLogger(__name__).info("Plugin loaded %s", plugin_name)