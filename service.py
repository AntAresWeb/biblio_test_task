def parse_param(params: list) -> dict:
    parsed = dict()
    key = ''
    for param in params:
        param = param.lower()
        match param:
            case '-a':
                key = 'author'
                parsed[key] = []
            case '-t':
                key = 'title'
                parsed[key] = []
            case '-y':
                key = 'year'
                parsed[key] = []
            case _:
                if len(key) > 0:
                    parsed[key].append(param)
    return parsed
