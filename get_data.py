import requests
import json
import csv


def get_data(url):
    page = requests.get(url)
    data = json.loads(page.text)['data']['list']

    return data


def preprocess_data_for_csv(data, parameters):
    output = []

    for el in data:
        loc_data = []
        for parameter in parameters:
            loc_data.append(el[parameter])

        output.append(loc_data)

    return output


def save_csv(data, path, headers):
    data = [headers] + data
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def get_and_save_data(parameters, headers, url, path_to_save):
    data = get_data(url)
    data_for_csv = preprocess_data_for_csv(data, parameters)
    save_csv(data_for_csv, path_to_save, headers)
