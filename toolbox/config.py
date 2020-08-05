import configparser
import ast
import pathlib

filePath = "/".join(str(pathlib.Path(__file__).parent.absolute()).split("/")[:-1]) + "/"
config = configparser.ConfigParser()
config.read(filePath + "/files/configuration.txt")

# ---------------------------------- WEB ------------------------------------

def is_headless():
    return ast.literal_eval(config.get("WEB", "headless"))

def get(string):
    return str(config["WEB"][string])