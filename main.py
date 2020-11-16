import argparse
import get_data
import json


def load_json(path):
    with open(path, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)

    return data


def main():
    parser = argparse.ArgumentParser(description='Сохранение данных')
    parser.add_argument('path', type=str,
                        help='Путь к файлу согласия или к папке с файлами согласий.')
    args = parser.parse_args()

    parameters = load_json('parameters.json')
    get_data.get_and_save_data(parameters=parameters['parameters'],
                               url=parameters['url'],
                               headers=parameters['headers'],
                               path_to_save=args.path)


if __name__ == '__main__':
    main()
