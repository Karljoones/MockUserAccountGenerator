import config
import csv

# Save the data as a CSV file
def save_as_csv(users):
    with open(config.output_filepath, mode='w', newline='') as users_file_csv:
        users_writer = csv.writer(users_file_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        users_writer.writerow(['UUID','Name', 'Email', 'Password', 'Locale', 'Country', 'Signup Time'])

        for user in users:
            users_writer.writerow([user.get_uuid(), user.name, user.email, user.get_password(), user.locale, user.country, user.signup_time])

        users_file_csv.close()

# Save as a .sql file
def save_as_sql(users):
    with open(config.sql_export_filepath, mode='w') as users_file_sql:
        users_file_sql.write(f"CREATE TABLE {config.sql_export_table_name} (uuid VARCHAR(255), name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), locale VARCHAR(255), country VARCHAR(255), signup_time FLOAT);\n")

        for user in users:
            users_file_sql.write(f"INSERT INTO {config.sql_export_table_name} (uuid, name, email, password, locale, country, signup_time) VALUES ('{user.get_uuid()}', '{user.name}', '{user.email}', '{user.get_password()}', '{user.locale}', '{user.country}', {user.signup_time});\n")

        users_file_sql.close()
