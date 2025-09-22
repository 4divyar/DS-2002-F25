.PHONY: all fetch analyze clean

# analyze is the default. but it has a prereq of fetching so the process doesn't skip that step
analyze: fetch
	@echo "Analyzing Data"
	bash ./analyze_data.sh
	@echo "METARS data fetch completed. Data saved into raw_metars directory."

fetch: 
	@echo "Fetching METARS Data"
	bash ./fetch_metars.sh
	@echo "Weather pipeline successfully completed."

clean:
	@echo "Cleaning Up"
	rm -rf raw_metars
	rm -rf weather_report.csv
	@echo "Cleanup complete - removed raw_metars and weather_reports.csv."

all: analyze
