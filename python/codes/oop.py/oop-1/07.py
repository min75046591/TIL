class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
print(
    MyClass.instance_method(instance)
)  # ('instance method', <__main__.MyClass object at0x…028F10>)
print(MyClass.class_method())  # ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method())  # static method


instance = MyClass()
print(
    instance.instance_method()
)  # ('instance method', <__main__.MyClass object at 0x0000…84EAF10>)
print(instance.class_method())  # ('class method', <class '__main__.MyClass'>)
print(instance.static_method())  # static method
