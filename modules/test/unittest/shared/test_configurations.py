import json

from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.shared.configurations import Configurations


def test_loading_config_values_works():
    actual = Configurations.get_config_with_key(Module.LABEL, Key.SAVING_PATH)
    with open("config.json") as f:
        data = json.load(f)
    expected = data["label"]["saving-path"]
    assert actual == expected


def test_loading_config_has_right_value():
    actual = Configurations.get_config_with_key(Module.TRAIN, Key.TRAIN)
    expected = 0.3
    assert actual == expected
