import configparser

def config(section, option, default=None):
    c = configparser.ConfigParser()
    c.read('.env')

    if c.has_option(section, option):
        return c[section][option]
    else:
        return default
