class Myclass:

    def instance_method(self):
        return 'instance method', self
    
    @classmethod
    def class_method(cls):
        return 'class method', cls
    
    @staticmethod
    def static_method():
        return 'static method'
    
# 클래스가 전부 다 호출해보기
instance = Myclass()

print(Myclass.instance_method(instance))
print(Myclass.class_method(instance))
print(Myclass.static_method(instance))

