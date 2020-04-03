import os
import pathlib

__root_location__ = str(pathlib.Path(__file__).parent.parent.absolute())

LOCATIONS = {"ROOT": __root_location__}
LOCATIONS.update({"DATA": __root_location__ + os.sep + "data"})
LOCATIONS.update({"CONFIG": __root_location__ + os.sep + "data" + os.sep + "config"})
LOCATIONS.update({"CONFIG_DEFAULT": __root_location__ + os.sep + "data" + os.sep + "config" + os.sep + "default"})
LOCATIONS.update({"SAMPLES": __root_location__ + os.sep + "data" + os.sep + "samples"})
LOCATIONS.update({"SAMPLES_DEFAULT": __root_location__ + os.sep + "data" + os.sep + "samples" + os.sep + "default"})
