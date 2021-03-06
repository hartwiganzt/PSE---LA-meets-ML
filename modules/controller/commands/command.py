from typing import List, Dict, Optional
from modules.controller.commands.key import Key
from modules.controller.commands.module import Module
from modules.exception.excpetions import IllegalArgumentException
from modules.shared.configurations import Configurations


##  Interface for the module specific commands
class Command:

    def __init__(self):
        self.__module_name: Module = Module.UNDEFINED
        self.__arguments: Dict[Key, str] = {}
        self.__valid_short_arguments: Dict[str, Key] = {}
        self.__valid_long_arguments: Dict[str, Key] = {}
        self.__required_arguments: List[Key] = []

    @property
    def module_name(self) -> Module:
        return self.__module_name

    @module_name.setter
    def module_name(self, module: Module) -> None:
        self.__module_name = module

    @property
    def arguments(self) -> Dict[Key, str]:
        return self.__arguments

    @arguments.setter
    def arguments(self, arguments: Dict[Key, str]) -> None:
        self.__arguments = arguments

    @property
    def required_arguments(self) -> List[Key]:
        return self.__required_arguments

    @required_arguments.setter
    def required_arguments(self, args: List[Key]) -> None:
        self.__required_arguments = args

    @property
    def valid_short_arguments(self) -> Dict[str, Key]:
        return self.__valid_short_arguments

    @valid_short_arguments.setter
    def valid_short_arguments(self, args: Dict[str, Key]) -> None:
        self.__valid_short_arguments = args

    @property
    def valid_long_arguments(self) -> Dict[str, Key]:
        return self.__valid_long_arguments

    @valid_long_arguments.setter
    def valid_long_arguments(self, args: Dict[str, Key]) -> None:
        self.__valid_long_arguments = args

    ##  can be called the execute the module
    def execute(self) -> None:
        self.validate()

    ##  will be called in the command execution
    def validate(self) -> None:
        for arg in self.required_arguments:
            if arg not in self.arguments:
                raise IllegalArgumentException("%s is required" % arg)

    def __add_default_args(self) -> None:
        for key, value in self.arguments.items():
            if value is None:
                self.arguments[key] = Configurations.get_config_with_key(self.module_name, key)

    ##  parses the string list into a dict of args
    #
    #   @param args the list retrieved by the input
    def set_args(self, arg_list: List[str]) -> None:
        while len(arg_list) != 0:
            next_key = arg_list.pop(0)
            key: Key = self.__get_key(next_key)
            value: str = ""
            if not arg_list[0].startswith("-"):
                value = arg_list.pop(0)
            self.arguments[key] = value
        self.__add_default_args()

    def __get_key(self, next_key: str) -> Key:
        if next_key.startswith("--") and next_key[2:] in self.valid_long_arguments:
            key: Key = self.valid_long_arguments[next_key[2:]]
        elif next_key.startswith("-") and next_key[1:] in self.valid_short_arguments:
            key: Key = self.valid_short_arguments[next_key[1:]]
        else:
            raise IllegalArgumentException("%s is not a valid argument." % next_key)
        return key

    def get_int_value(self, key: Key) -> Optional[int]:
        if key in self.arguments:
            return int(self.arguments.get(key))
        return None
