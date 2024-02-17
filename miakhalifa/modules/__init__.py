import logging
from os.path import dirname, basename, isfile
import glob

LOAD = []
NO_LOAD = []
LOGGER = logging.getLogger(__name__)

def __list_all_modules():
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD or NO_LOAD:
        to_load = LOAD if LOAD else all_modules

        if not all(mod in all_modules for mod in to_load):
            LOGGER.error("Invalid load order names. Quitting.")
            quit(1)

        if NO_LOAD:
            LOGGER.info("Not loading: %s", NO_LOAD)
            return [item for item in to_load if item not in NO_LOAD]

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
LOGGER.info("Modules to load: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
