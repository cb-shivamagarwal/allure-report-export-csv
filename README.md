# allure-report-export-csv
Creates a CSV containing all tests with exceptions and stack trace for failing tests.

## How to use ?
1. Download the `allure-report.zip` from allure and extract it. The following screenshot illustrates the location where the download link is present.


<img width="1502" alt="Screenshot 2022-07-13 at 8 02 52 PM" src="https://user-images.githubusercontent.com/98250333/178759931-ea1785c4-6d56-4ceb-b8ed-c3cb5718a61a.png">

2. Copy the python script named `generate_csv.py` from this repository and paste it in `allure-report/data/generate_csv.py`

3. Open the terminal inside `allure-report/data` and execute `python generate_csv.py`

4. This command would create a csv file `allure-report/data/final.csv` - the required CSV
