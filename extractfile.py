import csv

def extract_clients(_file):
    with open("./input/clients.csv", "r") as f:
        reader = csv.DictReader(f)
        cli = list(reader)
        return cli