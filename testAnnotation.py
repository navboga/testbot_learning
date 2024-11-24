# _annotations__
# О чем еще не сказал, так это о том, где объекты хранят аннотации типов. Для этого существует специальный атрибут __annotations__, который хранит аннотации в виде словаря с ключами - названиями переменных и значениями - их типами.
# Пример. Функция get_string, получающая на вход строку и число, а возвращающая строку.

def get_string(string: str,numb: int) ->str:
    return string * numb

print(get_string('Liverpool ', 11))

print(get_string.__annotations__)
