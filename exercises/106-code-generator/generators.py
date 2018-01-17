'''Code generators for transactions.'''
from parser import Array, Comment, DataType


def generate_cpp(elements):
    def generate_type(data):
        texts = [f'class {data.name} {{']
        for field in data.fields:
            name, value_type, comment = field
            if isinstance(value_type, Array):
                if len(value_type.length) > 0:
                    value_type = (f'std::array<{value_type.inner_type}, '
                                  f'{value_type.length}>')
                else:
                    value_type = f'std::vector<{value_type.inner_type}>'
            comment = generate_comment(comment)
            texts.append(f'    {value_type} {name}; {comment}')
        texts.append('};')
        return '\n'.join(texts)

    def generate_comment(comment):
        return f'//{comment.text}' if len(comment.text) > 0 else ''

    ELM_GENERATORS = {
            DataType: generate_type,
            Comment: generate_comment,
            }
    return '\n'.join([ELM_GENERATORS[type(elm)](elm) for elm in elements])


def generate_py(elements):
    def translate(typename):
        TYPENAMES = {
                'char': 'str'
                }
        return TYPENAMES[typename] if typename in TYPENAMES else typename

    def generate_type(data):
        texts = [f'class {data.name}(NamedTuple):']
        for field in data.fields:
            name, value_type, comment = field
            if isinstance(value_type, Array):
                if value_type.inner_type == 'char':
                    value_type = 'str'
                else:
                    value_type = f'List[{translate(value_type.inner_type)}]'
            comment = generate_comment(comment)
            texts.append(f'{name}: {value_type} {comment}')
        return '\n    '.join(texts)

    def generate_comment(comment):
        return f'#{comment.text}' if len(comment.text) > 0 else ''

    ELM_GENERATORS = {
            DataType: generate_type,
            Comment: generate_comment,
            }

    return '\n'.join([ELM_GENERATORS[type(elm)](elm) for elm in elements])
