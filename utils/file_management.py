import config
import csv
import os
from utils.decorators import time_measurement_decorator

# Create the output folder
def create_output_folder():
    if not os.path.exists(config.export_directory):
        os.makedirs(config.export_directory)
        print(f"Directory {config.export_directory} created")

# Save the data as a CSV file
@time_measurement_decorator
def save_as_csv(users):
    with open(f"{config.export_directory}/{config.csv_export_filename}", mode='w', newline='') as users_file_csv:
        users_writer = csv.writer(users_file_csv, delimiter=config.csv_export_delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if config.csv_include_headers:
            users_writer.writerow(['UUID','Name', 'Email', 'Password', 'Locale', 'Country', 'Signup Time'])

        for user in users:
            users_writer.writerow([user.get_uuid(), user.name, user.email, user.get_password(), user.locale, user.country, user.signup_time])

        users_file_csv.close()

# Save as a .sql file
@time_measurement_decorator
def save_as_sql(users):
    with open(f"{config.export_directory}/{config.sql_export_filename}", mode='w') as users_file_sql:
        # Drop table, if option is enabled within `config.py`
        if config.sql_drop_table_if_exists:
            users_file_sql.write(f"DROP TABLE IF EXISTS {config.sql_export_table_name};\n")

        # Create table, if option is enabled within `config.py`
        if config.sql_create_table:
            users_file_sql.write(f"CREATE TABLE {config.sql_export_table_name} (uuid VARCHAR(255), name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), locale VARCHAR(255), country VARCHAR(255), signup_time FLOAT, PRIMARY KEY ({config.sql_primary_key}));\n")

        for user in users:
            users_file_sql.write(f"INSERT INTO {config.sql_export_table_name} (uuid, name, email, password, locale, country, signup_time) VALUES ('{user.get_uuid()}', '{user.name}', '{user.email}', '{user.get_password()}', '{user.locale}', '{user.country}', {user.signup_time});\n")

        users_file_sql.close()