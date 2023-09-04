# para obter os pacotes POST/GET
from wiredseleniumdf import get_driver

driver = get_driver(
    save_folder="c:\\requestsdfs",
    stop_keys="ctrl+alt+e",
    scan_time=10,
)
driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")