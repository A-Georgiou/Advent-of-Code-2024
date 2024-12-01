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
                parsed_values = [value_type(val) for value_type, val in zip(value_types, values)]
                parsed_input.append(parsed_values)
            return parsed_input