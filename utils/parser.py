class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_input(self, value_types):
        with open(self.file_path, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            parsed_input = []

            for line in lines:
                values = line.split()
                if callable(value_types):
                    parsed_input.append([value_types(val) for val in values])
                elif isinstance(value_types, list):
                    parsed_input.append([value_type(val) for value_type, val in zip(value_types, values)])
                else:
                    raise ValueError("Invalid value_types. Must be callable or list of callables.")
            return parsed_input