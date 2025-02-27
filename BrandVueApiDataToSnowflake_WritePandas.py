import pandas as pd
from datetime import datetime, timedelta
from calendar import monthrange
from snowflake.snowpark import Session
from BrandVueApiShim import get_weightings, get_survey_responses, get_survey_respondents

# Parameters
year = 2025
month = 1
role = 'SYSADMIN'
database = 'zTmpTestBrandVueSurveyApi'
schema = 'public'

# Snowflake setup
connection_params = { 'connection_name': 'default' }
session = Session.builder.configs(connection_params).create()
session.use_role(role)
session.use_database(database)
session.use_schema(schema)

# Fetch and load data into Snowflake
surveyset = 'UK'
date = datetime(year, month, 1)

weightings = pd.DataFrame(get_weightings(surveyset, date)['value'])
survey_responses = []
survey_respondents = []

for i in range(monthrange(year, month)[1]):
    day = date + timedelta(days=i)
    survey_responses.extend(get_survey_responses(surveyset, 'brand', day))
    survey_respondents.extend(get_survey_respondents(surveyset, day))

weightings_df = pd.DataFrame(weightings)
response_df = pd.DataFrame(survey_responses)
respondent_df = pd.DataFrame(survey_respondents)

print(f'Writing data to Multipliers')
session.write_pandas(weightings_df, 'Multipliers', auto_create_table=True, overwrite=True)

print(f'Writing data to SurveyResponses')
session.write_pandas(response_df, 'SurveyResponses', auto_create_table=True, overwrite=True)

print(f'Writing data to SurveyProfiles')
session.write_pandas(respondent_df, 'SurveyProfiles', auto_create_table=True, overwrite=True)

# Close the session
session.close()