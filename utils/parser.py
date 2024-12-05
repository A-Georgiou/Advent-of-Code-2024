class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def _read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except Exception as e:
            raise IOError(f"An error occurred while reading the file: {e}")

    def parse_lines(self, value_types, delimiter=None):
        content = self._read_file()
        lines = content.splitlines()
        parsed_input = []

        for line_num, line in enumerate(lines, start=1):
            try:
                values = line.split(delimiter) if delimiter else line.split()
                if callable(value_types):
                    parsed_input.append([value_types(val) for val in values])
                elif isinstance(value_types, list):
                    parsed_input.append([value_type(val) for value_type, val in zip(value_types, values)])
                else:
                    raise ValueError("Invalid value_types. Must be callable or list of callables.")
            except Exception as e:
                raise ValueError(f"Error parsing line {line_num}: {line}. {e}")
        return parsed_input

    def parse_sections(self, value_type, section_delimiter="\n\n"):
        content = self._read_file()
        sections = content.strip().split(section_delimiter)
        try:
            return [value_type(section) for section in sections]
        except Exception as e:
            raise ValueError(f"Error parsing sections: {e}")
    
    def parse_whole_input(self, value_type):
        content = self._read_file()
        try:
            return value_type(content)
        except Exception as e:
            raise ValueError(f"Error parsing whole input: {e}")