DEFAULTS = {
        }

templates = {
        'cpp': {
            'line-comment': '//{comment}',
            'type-def': {
                'begin': 'class {type_name} {{',
                'field': '{field_type} {field_name};',
                'end': '}};',
                },
            'types': {
                'str': 'std::string',
                'char': 'char',
                'array': 'std::array<{inner_type}, {size}>',
                'vector': 'std::vector<{inner_type}>',
                },
            },
        'py': {
            'line-comment': '#{comment}',
            'type-def': {
                'begin': 'class {type_name}:',
                'field': '{field_name}: {field_type}',
                'end': '',
                },
            'types': {
                'str': 'str',
                'char': 'str',
                'array': 'List[{inner_type}]',
                'vector': 'List[{inner_type}]',
                }
            }
        }
