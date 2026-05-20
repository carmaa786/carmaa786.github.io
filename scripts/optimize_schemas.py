import os
import re
import json

# Define the target city files and their configuration
CITY_CONFIGS = {
    "doorstep-car-washing-service-in-delhi/index.html": {
        "city_name": "Delhi",
        "locality": "Delhi",
        "region": "Delhi",
        "postal_code": "110001",
        "latitude": 28.6139,
        "longitude": 77.2090
    },
    "doorstep-car-washing-service-in-noida/index.html": {
        "city_name": "Noida",
        "locality": "Noida",
        "region": "Uttar Pradesh",
        "postal_code": "201301",
        "latitude": 28.5355,
        "longitude": 77.3910
    },
    "doorstep-car-washing-service-in-gurgaon/index.html": {
        "city_name": "Gurgaon",
        "locality": "Gurgaon",
        "region": "Haryana",
        "postal_code": "122001",
        "latitude": 28.4595,
        "longitude": 77.0266
    },
    "doorstep-car-washing-service-in-faridabad/index.html": {
        "city_name": "Faridabad",
        "locality": "Faridabad",
        "region": "Haryana",
        "postal_code": "121001",
        "latitude": 28.4089,
        "longitude": 77.3178
    },
    "doorstep-car-washing-service-in-gaziabad/index.html": {
        "city_name": "Ghaziabad",
        "locality": "Ghaziabad",
        "region": "Uttar Pradesh",
        "postal_code": "201001",
        "latitude": 28.6692,
        "longitude": 77.4538
    }
}

DEFAULT_OPENING_HOURS = [
    {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ],
        "opens": "07:00",
        "closes": "20:00"
    }
]

def update_json_ld(json_str, config):
    try:
        data = json.loads(json_str)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return json_str

    modified = False

    # Check if this is a @graph structure
    if isinstance(data, dict) and "@graph" in data:
        for idx, item in enumerate(data["@graph"]):
            if isinstance(item, dict) and item.get("@type") == "AutomotiveBusiness":
                # Update address
                existing_address = item.get("address", {})
                new_address = {
                    "@type": "PostalAddress"
                }
                # Keep streetAddress if present
                if "streetAddress" in existing_address:
                    new_address["streetAddress"] = existing_address["streetAddress"]
                
                new_address.update({
                    "addressLocality": config["locality"],
                    "addressRegion": config["region"],
                    "postalCode": config["postal_code"],
                    "addressCountry": "IN"
                })
                item["address"] = new_address

                # Update geo to floats
                item["geo"] = {
                    "@type": "GeoCoordinates",
                    "latitude": config["latitude"],
                    "longitude": config["longitude"]
                }

                # Update or add areaServed
                item["areaServed"] = {
                    "@type": "City",
                    "name": config["city_name"]
                }

                # Add openingHoursSpecification if missing
                if "openingHoursSpecification" not in item:
                    item["openingHoursSpecification"] = DEFAULT_OPENING_HOURS

                modified = True

    if modified:
        # Dump back to JSON with 4 spaces indent, preserving unicode
        updated_json_str = json.dumps(data, indent=4, ensure_ascii=False)
        return updated_json_str
    
    return json_str

def main():
    base_dir = r"C:\Users\jugal\OneDrive\Desktop\carmaa-2026"
    print("Starting JSON-LD schema optimization...\n")

    for rel_path, config in CITY_CONFIGS.items():
        file_path = os.path.join(base_dir, rel_path)
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            continue

        print(f"Processing: {rel_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regular expression to find JSON-LD blocks
        pattern = re.compile(r'(<script\s+type="application/ld\+json">)(\{.*?\})(</script>)', re.DOTALL)
        
        matches = list(pattern.finditer(content))
        if not matches:
            print(f"  No JSON-LD block found in {rel_path}")
            continue

        new_content = content
        offset = 0
        for match in matches:
            tag_open = match.group(1)
            json_payload = match.group(2)
            tag_close = match.group(3)

            # Update the JSON payload
            updated_json = update_json_ld(json_payload, config)
            
            if updated_json != json_payload:
                # Add proper indent offset to match existing layout
                # The existing block starts right after <script...>
                # Let's clean up indentation formatting slightly if needed,
                # but standard json.dumps is usually perfect.
                replacement = tag_open + updated_json + tag_close
                start = match.start() + offset
                end = match.end() + offset
                new_content = new_content[:start] + replacement + new_content[end:]
                offset += len(replacement) - (end - start)
                print(f"  Successfully updated AutomotiveBusiness schema in {rel_path}")

        if new_content != content:
            with open(file_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(new_content)
            print(f"  Saved changes to {rel_path}")
        else:
            print(f"  No changes needed for {rel_path}")

if __name__ == "__main__":
    main()
