# inbuilt libraries
from urllib.parse import urljoin

# third-party libraries
import pathlib
import logging
from model.template import render_j2_template


LOGGER = logging.getLogger(__name__)
SCHEMAS = pathlib.Path(__file__).resolve().parent
VERSION = '0.1'

class Dataset:
    def __init__(
        self, 
        dataset_raw, 
        base_url: str, 
        mappings_folder: str = "ckan2pycsw/mappings",
        csw_schema: str = "iso19139_base"):
        """
        Constructor of the Dataset class.

        Attributes
        ----------
        dataset_raw: Dataset data from CKAN API.
        base_url: str. URL of the CKAN endpoint retrieved from envvars.
        mappings_folder: str. Folder of the mappings.
        csw_schema: str. Dataset dict schema to transform CKAN Schema to CSW.
        """
        self.dataset_raw = dataset_raw
        self.name = dataset_raw["name"]
        self.url = urljoin(base_url, "dataset/" + self.name + "/")
        self.mappings_folder = mappings_folder
        self.csw_schema = csw_schema
        self.render_template = render_j2_template(mcf=self.dataset_raw, schema_type="ckan",url=self.url, template_dir=self.csw_schema, mappings_folder=self.mappings_folder)