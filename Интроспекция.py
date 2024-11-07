def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение всех атрибутов и методов объекта
    attributes = []
    methods = []
    for attr in dir(obj):
        if attr.startswith('__') and attr.endswith('__'):
            continue  # Игнорируем встроенные магические методы
        attr_value = getattr(obj, attr, None)
        if callable(attr_value):
            methods.append(attr)
        else:
            attributes.append(attr)

    # Определение модуля, к которому принадлежит объект
    module = getattr(obj, '__module__', 'built-in' if obj_type in dir(__builtins__) else None)

    # Словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)
