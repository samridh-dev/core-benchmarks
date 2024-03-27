def parse_file(file_path):
    """
    Parses a file with the given format into a dictionary.
    
    :param file_path: Path to the file to be parsed
    :return: Dictionary with the size as keys and a list of (thread, time) tuples as values
    """
    data_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue  # Skip empty lines
            parts = line.strip().split(' ')
            size = parts[1]  # After '?'
            thread_count = int(parts[3])  # After '-'
            time = float(parts[5])  # After ':'
            
            if size not in data_dict:
                data_dict[size] = []
            data_dict[size].append((thread_count, time))
            
    return data_dict
