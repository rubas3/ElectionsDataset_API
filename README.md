# Elections API Project

This project converts the Elections API into a dataset and exposes it again as a Flask API with custom endpoints.

## Project Steps

1. **Data Compilation**
   - `script_to_compile_data.py` fetches data from the Elections API for 2008, 2013, 2018.
   - Generates clean CSV/JSON dataset (excludes "geom" field).

2. **Flask API**
   - `app.py` exposes the following endpoints:
     - **/province**: Province-wise historical data
     - **/history**: Year-wise data, optionally filtered by province

3. **Usage**
   - Run `script_to_compile_data.py` to generate dataset.
   - Install dependencies:  
     ```bash
     pip install -r flask_api/requirements.txt
     ```
   - Run API:  
     ```bash
     python flask_api/app.py
     ```

## Notes
- Screenshots of API endpoints are in the submission PDF.
- Dataset is dynamically created when running the script.
