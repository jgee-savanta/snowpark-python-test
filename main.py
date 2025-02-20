from snowflake.snowpark import Session
from snowflake.core import Root

connection_params = {
    "account": "LK43159.uk-south.azure",
    "user": "jack.gee@savanta.com",
    "role": "SYSADMIN",
    "authenticator": "externalbrowser"
}

session = Session.builder.configs(connection_params).create()
root = Root(session)

databases_df = session.sql("SHOW DATABASES")

for row in databases_df.collect():
    print(row[1])  # The name of the database is in the second column

session.close()
