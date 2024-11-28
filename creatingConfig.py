# Import module
import configparser

# Create a configparser object
config_object = configparser.ConfigParser()
# Add sections to the configuration object
config_object["xml"]={"Directory" : "8080", "host" : "0.0.0.0"}

# Save the configuration file
with open("config.ini","w") as file_object:
    config_object.write(file_object)