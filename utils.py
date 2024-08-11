import logging
# import pdflatex
from jinja2 import Environment, FileSystemLoader
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from ruamel.yaml.error import YAMLError

logger = logging.getLogger(__name__)
yaml = YAML(typ='safe', pure=True)
def read_jobfile(filename: str) -> str:
    with open(filename, "r",  encoding="utf8") as stream:
        try:
            return stream.read().strip()
        except OSError as e:
            logger.error(f"The {filename} could not be read.")
            raise e
        
        
def read_yaml(yaml_text: str = "", filename: str = "") -> dict:
    if not yaml_text and not filename:
        logger.warning("Neither yaml text nor filename have been provided.")
        return None
    if yaml_text:
        try:
            return yaml.load(yaml_text)
        except YAMLError as e:
            logger.error(f"The text could not be read.")
            raise e
    with open(filename, "r") as stream:
        try:
            return yaml.load(stream)
        except YAMLError as e:
            logger.error(f"The {filename} could not be read.")
            raise e
        except Exception as e:
            logger.error(
                f"The {filename} could not be written due to an unknown error."
            )
            raise e
