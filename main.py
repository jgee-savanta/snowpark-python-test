from snowflake.snowpark import Session
from snowflake.core import Root

connection_params = { "connection_name": "LK43159.uk-south.azure" }

session = Session.builder.configs(connection_params).create()
root = Root(session)

tables_df = session.sql("SHOW TABLES IN SCHEMA VUEEXPORT_TEST.VUE")

for row in tables_df.collect():
    print(row[1])

session.close()
