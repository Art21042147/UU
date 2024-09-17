import inspect
from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__

    obj_module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'Built-in'

    attributes = [attr for attr in dir(obj)
                  if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    methods = [method for method in dir(obj)
               if callable(getattr(obj, method)) and not method.startswith('__')]

    extra_info = {}

    if isinstance(obj, (int, float, str)):
        extra_info['is_numeric'] = isinstance(obj, (int, float))
        extra_info['length'] = len(obj) if hasattr(obj, '__len__') else 'N/A'

    if inspect.isfunction(obj):
        signature = inspect.signature(obj)

        annotations = obj.__annotations__ if hasattr(obj, '__annotations__') else {}

        docstring = inspect.getdoc(obj) if obj.__doc__ else 'No docstring available'

        extra_info['name'] = obj.__name__
        extra_info['signature'] = str(signature)
        extra_info['annotations'] = annotations
        extra_info['docstring'] = docstring

        closure = obj.__closure__
        if closure:
            closure_vars = [cell.cell_contents for cell in closure]
            extra_info['closure_vars'] = closure_vars

    result = {
        'type': obj_type,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods,
        'extra_info': extra_info
    }

    return result


class UrbanPython:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def my_method(self):
        return f'Hello, {self.name}!'


my_obj = UrbanPython('Urban', 'Python')

info = introspection_info(my_obj)

pprint(info)

func_info = introspection_info(introspection_info)
pprint(func_info)
