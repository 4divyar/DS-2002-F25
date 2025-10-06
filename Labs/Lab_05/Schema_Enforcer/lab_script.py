import pandas as pd
import csv
import json

# Part 1
# Task 1
# create dataframe
data = {
    'student_id': [12345, 67890, 24680, 13579, 36912],
    'major': ['Computer Science', 'Data Science', 'English', 'Chemical Engineering', 'History'],
    'GPA': [3, 3.4, 3.87, 2.1, 2],
    "is_cs_major": [True, False, 'No', False, 'No'],
    'credits_taken': ['10.5', '32', '74', 20, '56']
}

df = pd.DataFrame(data) # make into df so there are headers
df.to_csv("raw_survey_data.csv", index=False) # write to csv (no index needed)

#####

# Task 2
dict = [
  {
    "course_id": "DS2002",
    "section": "001",
    "title": "Data Science Systems",
    "level": 2000,
    "instructors": [
      {"name": "Austin Rivera", "role": "Primary"}, 
      {"name": "Heywood Williams-Tracy", "role": "TA"} 
    ]
  },
  {
    "course_id": "STAT4630",
    "title": "Statistical Machine Learning",
    "level": 4000,
    "instructors": [
      {"name": "Shan Yu", "role": "Primary"}
    ]
  },
  {
    "course_id": "STAT4170",
    "title": "Financial Time Series and Forecasting",
    "level": 4000,
    "instructors": [
      {"name": "Jeffery Woo", "role": "Primary"}
    ]
  },
  {
    "course_id": "CS3710",
    "title": "Intro to Cybersecurity",
    "level": 3000,
    "instructors": [
      {"name": "Angela Orebaugh", "role": "Primary"}
    ]
  }
]

# write to json file
file_path = "raw_course_catalog.json"
with open(file_path, 'w') as json_file:
    json.dump(dict, json_file, indent=4)

#####

# Part 2
# Task 3
rawsurveydf = pd.read_csv('raw_survey_data.csv')

rawsurveydf['is_cs_major'] = rawsurveydf['is_cs_major'].replace({'Yes': True, 'No': False})
rawsurveydf['credits_taken'] = rawsurveydf['credits_taken'].astype(float)
rawsurveydf['GPA'] = rawsurveydf['GPA'].astype(float)

rawsurveydf.to_csv("cleaned_survey_data.csv", index=False)

# Task 4
with open('raw_course_catalog.json', 'r') as file:
    rawcoursedf = json.load(file)

normalized = pd.json_normalize(rawcoursedf, record_path=['instructors'], 
                               meta=['course_id', 'title', 'level'])

normalized.to_csv('clean_course_catalog.csv', index=False)