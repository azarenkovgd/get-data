# Загрузка данных с http://dop.edu.ru

### Установка (на ubuntu 20.04)
* Удостовериться что версия python > 3.5
* ```git clone https://github.com/azarenkovgd/get-data/```
* ```cd get-data```
* При необходимости установить virtual enviroment через ```apt-get install python3-venv```
* Создание venv ```python3 -m venv```.
* Активация ```source bin/activate```
* Установка требуемых библиотек ```pip install -r requirements.txt```


### Запуск
Cкрипт запуска программы - ```main.py```

Аргументы:

```path``` - куда сохранить файл csv.

Пример:

```python3 main.py data.csv```
