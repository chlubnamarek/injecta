from injecta.service.argument.DictArgument import DictArgument
from injecta.service.argument.ListArgument import ListArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.config.ConfigLoader import TaggedServices
from injecta.service.argument.TaggedServicesArgument import TaggedServicesArgument

class ArgumentParser:

    def parse(self, argument):
        if isinstance(argument, str):
            if argument[0:1] == '@':
                return ServiceArgument(argument[1:])

            return PrimitiveArgument(argument)

        if isinstance(argument, TaggedServices):
            return TaggedServicesArgument(argument.val)

        if isinstance(argument, (int, bool)):
            return PrimitiveArgument(argument)

        if isinstance(argument, list):
            return ListArgument(list(map(self.parse, argument)))

        if isinstance(argument, dict):
            return DictArgument({k: self.parse(v) for k, v in argument.items()})

        raise Exception('Unexpected argument type: {}'.format(type(argument)))