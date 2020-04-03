import os
import pathlib

__root_location__ = str(pathlib.Path(__file__).parent.parent.absolute())

LOCATIONS = {"ROOT": __root_location__}
LOCATIONS.update({"DATA": __root_location__ + os.sep + "data"})
LOCATIONS.update({"SAMPLES": __root_location__ + os.sep + "data" + os.sep + "samples"})
