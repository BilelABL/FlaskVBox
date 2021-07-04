import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

if __name__ == "__main__":
    filepath = "app.yaml"
    data = yaml_loader(filepath)
    print(data)