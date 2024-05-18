# Runtime configuration
users_to_generate = 10_000

# Files (output)
export_directory = 'output'
csv_export_filename = 'users.csv'
sql_export_filename = 'users.sql'

# Files (input)
first_names_filepath = 'data/names_first.txt'
last_names_filepath = 'data/names_last.txt'
domains_filepath = 'data/domains.txt'
countries_and_locales_filepath = 'data/countries_and_locales.csv'

# SQL
sql_export = True
sql_export_table_name = 'USERS'
sql_drop_table_if_exists = True
sql_create_table = True
sql_primary_key = 'userid'

# CSV
csv_export = True
csv_export_delimiter = ','
csv_include_headers = True

# Debug
verbose_processing = False
verbose_debugging = True