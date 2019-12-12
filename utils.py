import configparser


def fill_config(port):
    config = configparser.ConfigParser()
    config['DEFAULT']['port'] = str(port)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
