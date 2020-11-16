from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def load_config(path):
    with open(path, 'r') as f_stream:
        return load(f_stream, Loader=Loader)


UNSECRET_KEY = 'fooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
APP_CONFIG = load_config('config.yaml')
