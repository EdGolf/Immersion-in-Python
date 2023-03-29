def get_argument_dict(**kwargs) -> dict[any, str]:
    names, values = zip(*kwargs.items())
    values_hashable = map(convert_to_hashable, values)
    return dict(zip(values_hashable, names))


def convert_to_hashable(object):
    return object if isinstance(object, (str, int, bool, float, tuple, frozenset)) else str(object)


print(get_argument_dict(arg1=58685, arg2="Hello World", arg3=[0, 1, 2, 3, 4, ], arg4={3, 2, 1, 0},
                        arg5=frozenset((5, 5, 5, 5))))
