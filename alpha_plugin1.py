import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from utils import utils
from helper import conftools

load_dotenv()
timeStamp = int(datetime.now(tz=timezone.utc).timestamp())
config_data = conftools.yaml_to_dictionary(os.path.join(os.getcwd(), 'static', 'config.yaml'))
xml = conftools.xml_load(os.path.join(os.getcwd(), 'static', 'mapping_Alpha_Adapter.xlsx'))
logger = conftools.load_logger(os.path.join(os.getcwd(), 'logs'), 'plugin.log')

def main():
    while True:
        utils.main(config_data, logger, xml)

if __name__ == '__main__':
    main()
