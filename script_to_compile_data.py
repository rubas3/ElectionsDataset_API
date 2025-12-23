import json, requests, csv

years = ['2008', '2013', '2018']
compiled_data = []

for year in years:
    url = f"https://api6.tplmaps.com/dawn_election_portal/assets/js/election_{year}.js"
    response = requests.get(url) 
    if response.status_code == 200:   
        try:
            json_str = response.text[14:]
            data = json.loads(json_str)
            for item in data:
                item.pop("geom", None)
                item["year"] = year
            compiled_data.extend(data)
            print(f"Loaded data for {year}")
        except Exception as e:
            print(f"Error parsing JSON for {year}: {e}")
    else:
        print(f"Failed to fetch data for {year}")
  
#save to json      
with open("compile_data.json", 'w', encoding='utf-8') as f:
    json.dump(compiled_data, f, indent=2, ensure_ascii=False)
    
# Save to CSV
if compiled_data:
    keys = compiled_data[0].keys()
    with open("compile_data.csv", 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(compiled_data)
        