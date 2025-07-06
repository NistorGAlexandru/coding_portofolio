import requests
import xml.etree.ElementTree as ET


url = "https://www.bnr.ro/nbrfxrates.xml"
r   = requests.get(url)
r.raise_for_status()

root = ET.fromstring(r.content)

ns = {"bnr": "http://www.bnr.ro/xsd"}

rate_elem = root.find(".//bnr:Rate[@currency='EUR']", namespaces=ns)
if rate_elem is None:
    raise ValueError("EUR rate not found in XML feed")

print("EUR →", rate_elem.text.strip())
