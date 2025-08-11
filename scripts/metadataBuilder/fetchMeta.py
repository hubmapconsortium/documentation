import os
import json
import re
import requests

BASE_TEMPLATE_URL = "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F{}"
# https://hubmapconsortium.github.io/ingest-validation-tools/facs/current/

templateIDs = [
    "c78c882d-ff27-473e-b318-540dc6e8034d", #Olink
    "20f1b25a-49dd-419e-a15d-ec02d396b7f7", #CyCif
    "df335a89-b470-4c2c-a4c9-e8db7f166d59", #FACS
    "24378678-d237-45ac-91c0-40e41d1e8a3e", #Seq-Scope
]

strip = [
    "@id",
    "@type",
    "schema:name",
    "schema:description",
]

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_assays():
    assays = []
    for id in templateIDs:
        url = BASE_TEMPLATE_URL.format(id)
        assay = fetch_data(url)
        props = assay.get("properties", {})
        assay_details = {
            "assayName": assay.get("schema:name", ""),
            "properties": []
        }
        print(f" Captured {assay_details['assayName']} details...")
        for property, prop_val in props.items():
            if property in strip:
                continue
            literal_values = []
            name = prop_val.get("skos:prefLabel", "")
            shortcode = prop_val.get("schema:name", "")
            type_ = prop_val.get("_ui", {}).get("inputType", "")
            constraints = []
            literals = []
            value = ""
            
            value_constraints = prop_val.get("_valueConstraints", {})
            # Assigned Values
            if value_constraints.get("branches"):
                branches = value_constraints.get("branches")
                
                if isinstance(branches, list):
                    for branch in branches:
                        name = branch.get("name")
                        uri = branch.get("uri")
                elif isinstance(branches, dict):
                    name = branches.get("name")
                    uri = branches.get("uri")
                
                constraints = branches
                if isinstance(constraints, list) and constraints and isinstance(constraints[0], dict) and 'uri' in constraints[0]:
                    value_HRAVS = str(constraints[0]['uri'])
                    # print(value_HRAVS)
                    value = fetch_by_HRAVS(constraints)
                    type_ = "Assigned Value"

            # YES / NO
            elif value_constraints.get("literals"):
                literals = value_constraints["literals"]
                for literal in literals:
                    if isinstance(literal, dict):
                        for key in ("label", "value", "prefLabel"):
                            if key in literal:
                                literal_values.append(str(literal[key]))
                                break
                        else:
                            literal_values.append(str(literal))
                    else:
                        literal_values.append(str(literal))
                type_ = "Radio"
                value = ",".join(literal_values)
            
            else:
                type_ = prop_val.get("_ui", {}).get("inputType", "")
                value = ""
            
            if name:
                assay_details["properties"].append({
                    "attribute": shortcode,
                    "label": name,
                    "type": type_.title() if isinstance(type_, str) else type_,
                    "description": prop_val.get("schema:description", ""),
                    "value": value,
                    "required": value_constraints.get("requiredValue")
                })
            
        assays.append(json.dumps(assay_details))
        title = f"{assay.get('schema:name', '')}.json"
        title = re.sub(r"[\s;]+", "-", title)
        os.makedirs("metaJSON", exist_ok=True)
        with open(os.path.join("metaJSON", title), "w") as f:
            json.dump(assay_details, f)

def fetch_by_HRAVS(details):
    detail = details[0];
    if detail.get("uri"):
        value_HRAVS = str(detail.get("uri"))
        
        match = re.search(r'#HRAVS_(\d+)', value_HRAVS)
        if match:
            hravs_id = match.group(1)
            valueSet = fetch_details(hravs_id)
            return valueSet

def fetch_details(url_id):
    BASE_URL ="https://data.bioontology.org/ontologies/HRAVS/classes/https%3A%2F%2Fpurl.humanatlas.io%2Fvocab%2Fhravs%23HRAVS_{}"
    url = BASE_URL.format(url_id)+"/children?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb&display=prefLabel&no_context=true"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    try:
        data = json.loads(response.text)
        collection = data.get("collection", [])
        values = [item.get("prefLabel") for item in collection if "prefLabel" in item]
    except Exception as e:
        print(f"Error parsing JSON for {url_id}: {e}")
        
    return values
  
def main():
    process_assays()

if __name__ == "__main__":
    main()