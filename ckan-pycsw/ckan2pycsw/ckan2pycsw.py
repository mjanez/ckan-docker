# inbuilt libraries
import logging
import pathlib
from configparser import ConfigParser
from urllib.parse import urljoin
import os

# third-party libraries
import requests
import pycsw.core.config
from pycsw.core import admin, metadata, repository, util
from pygeometa.core import read_mcf
from pygeometa.schemas.iso19139 import ISO19139OutputSchema

# custom functions
from config.log import log_file

# custom classes
from model.dataset import Dataset
from schemas.pygeometa.iso19139_inspire import ISO19139_inspireOutputSchema

# debug
import ptvsd


URL = os.environ["CKAN_URL"]
APP_DIR = os.environ["APP_DIR"]
CKAN_API = "api/3/action/package_search"
PYCSW_CKAN_SCHEMA = os.environ["PYCSW_CKAN_SCHEMA"]
PYCSW_OUPUT_SCHEMA = os.environ["PYCSW_OUPUT_SCHEMA"]
DEV_MODE = os.environ.get("DEV_MODE", None)  
MAPPINGS_FOLDER = "ckan2pycsw/mappings"
log_module = "[ckan2pycsw]"
OUPUT_SCHEMA = {
    'iso19139_inspire': ISO19139_inspireOutputSchema,
    'iso19139': ISO19139OutputSchema
}

def get_datasets(base_url):
    if not base_url.endswith('/'):
            base_url += '/'
    package_search = urljoin(base_url, CKAN_API)
    res = requests.get(package_search, params={"rows": 0})
    end = res.json()["result"]["count"]
    rows = 10
    for start in range(0, end, rows):
        res = requests.get(package_search, params={"start": start, "rows": rows})
        for dataset in res.json()["result"]["results"]:
            if dataset["type"] == "dataset":
                yield dataset

def main():
    log_file(APP_DIR + "/log")
    logging.info(f"{log_module}:ckan2pycsw | Version: 0.1")
    pycsw_config = ConfigParser()
    pycsw_config.read_file(open("pycsw.conf"))
    database = pycsw_config.get("repository", "database")
    table_name = pycsw_config.get("repository", "table", fallback="records")
    context = pycsw.core.config.StaticContext()

    # check if cite.db exists in folder, and delete it if it does
    database_path = "/" + database.split("//")[-1]
    if pathlib.Path(database_path).exists():
        os.remove(database_path)
    pycsw.core.admin.setup_db(
        database,
        table_name,
        "",
    )

    repo = repository.Repository(database, context, table=table_name)

    dcat_type = [
         "dataset", 
         "series", 
         "service"
         ]
    
    # Only iterate over dataset if dataset['dcat_type'] in dcat_type
    for dataset in (d for d in get_datasets(URL) if d["dcat_type"].rsplit('/', 1)[-1] in dcat_type):
                # Add a counter of errors and valids datasets

                d_dcat_type = dataset['dcat_type'].rsplit('/', 1)[-1]
                logging.info(f"{log_module}:ckan2pycsw | Metadata: {dataset['name']} [DCAT Type: {d_dcat_type.capitalize()}]")
                try:
                    dataset_metadata =  Dataset(dataset_raw=dataset, base_url=URL, mappings_folder=MAPPINGS_FOLDER,  csw_schema=PYCSW_CKAN_SCHEMA)
                    mcf_dict = read_mcf(dataset_metadata.render_template)
                    
                    # Select an output schema based on OUPUT_SCHEMA if not exists use ISO19139
                    if PYCSW_OUPUT_SCHEMA in OUPUT_SCHEMA:
                        iso_os = OUPUT_SCHEMA[PYCSW_OUPUT_SCHEMA]()
                        xml_string = iso_os.write(mcf=mcf_dict, mappings_folder=MAPPINGS_FOLDER)
                    else:
                        iso_os = ISO19139OutputSchema()
                        xml_string = iso_os.write(mcf=mcf_dict)


                    #TODO: DELETE Dumps to log
                    #print(xml_string,  file=open(APP_DIR + '/log/demo.xml', 'w', encoding='utf-8'))

                    # parse xml
                    record = metadata.parse_record(context, xml_string, repo)[0]
                    repo.insert(record, "local", util.get_today_and_now())
                except Exception as e:
                    logging.error(f"{log_module}:ckan2pycsw | Complete metadata in CKAN for: {dataset['name']} [DCAT Type: {d_dcat_type.capitalize()}] Error: {e}")
                    continue

    # Export records to Folder
    pycsw.core.admin.export_records(
         context, 
         database, 
         table=table_name, 
         xml_dirpath=APP_DIR + "/metadata/")

if __name__ == "__main__":
    if DEV_MODE == True:
        # Allow other computers to attach to ptvsd at this IP address and port.
        ptvsd.enable_attach(address=('0.0.0.0', 5678), redirect_output=True)

        # Pause the program until a remote debugger is attached
        ptvsd.wait_for_attach()
    main()