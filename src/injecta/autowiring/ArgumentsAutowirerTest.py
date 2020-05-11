import unittest
from injecta.autowiring.ArgumentResolver import ArgumentResolver
from injecta.autowiring.ArgumentsAutowirer import ArgumentsAutowirer
from injecta.dtype.DType import DType
from injecta.service.argument.PrimitiveArgument import PrimitiveArgument
from injecta.service.argument.ServiceArgument import ServiceArgument
from injecta.service.class_.ConstructorArgument import ConstructorArgument

class ArgumentsAutowirerTest(unittest.TestCase):

    def setUp(self):
        self.__argumentsAutowirer = ArgumentsAutowirer(ArgumentResolver())

    def test_basic(self):
        arguments = [
            PrimitiveArgument(123),
            ServiceArgument('my.module.ManuallyWiredClass'),
        ]
        constructorArguments = [
            ConstructorArgument('myNumber', DType('builtins', 'int')),
            ConstructorArgument('manuallyWiredService', DType('my.module.ManuallyWiredClass', 'ManuallyWiredClass')),
            ConstructorArgument('autowiredService', DType('my.module.OtherClass', 'OtherClass')),
        ]
        classes2Services = {
            'my.module.OtherClass': {'OtherClass': ['my.module.OtherClass']}
        }

        newArguments = self.__argumentsAutowirer.autowire(
            'my.module.MyClass',
            arguments,
            constructorArguments,
            classes2Services,
        )

        self.assertEqual(3, len(newArguments))
        self.assertEqual(PrimitiveArgument(123), newArguments[0])
        self.assertEqual(ServiceArgument('my.module.ManuallyWiredClass'), newArguments[1])
        self.assertEqual(ServiceArgument('my.module.OtherClass'), newArguments[2])

if __name__ == '__main__':
    unittest.main()