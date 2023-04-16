# UAddress - Deepparse model

Модель uaddress для библиотеки [deepparse](https://github.com/GRAAL-Research/deepparse)

> Read this in other language: [English](README.en.md), [Русский](README.md), [Український](README.ua.md)

# Требования
* python3
* deepparse
* pandas
* colored

## Установка зависимостей
```shell
pip3 install -r requirements.txt
```

## Подготовка данных
```shell
python3 pretrain.py
```

## Обучение модели
```shell
python3 train.py
```

![train](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/train.gif?raw=true)

## Пример
```shell
python3 example.py
```

![example](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/example.gif?raw=true)

## Структура
| Файл                          | Описание                                                  |
| :-------------                | :-------------                                            |
| example.py                    | Пример разбора адреса на типы                             |
| train.py                      | Обучения модели                                           |
| pretrain.py                   | Подготовка данных для обучения модели                     |
| check_data.py                 | Проверка данных для обучения модели                       |
| improver.py                   | Улучшение адреса                                          |
| data/data.csv                 | Данные для обучения модели                                |
| data/test.csv                 | Данные для проверки модели после обучения                 |
| data/raw.csv                  | Сырые данные для подготовки данных для обучения модели    |
| data/uaddress.ckpt            | Модель после обучения (bpemb)                             |
| data/uaddress_fasttext.ckpt   | Модель после обучения (Fasttext)                          |

## Типы
| Название                  | Описание                                      |
| :-------------            | :-------------                                |
| Country                   | Страна                                        |
| RegionType                | Тип области                                   |
| Region                    | Область                                       |
| CountyType                | Тип района                                    |
| County                    | Район                                         |
| SubLocalityType           | Тип подрайона                                 |
| SubLocality               | Подрайон                                      |
| LocalityType              | Тип населённого пункта                        |
| Locality                  | Населённый пункт                              |
| StreetType                | Тип улицы                                     |
| Street                    | Улица                                         |
| HousingType               | Тип корпуса                                   |
| Housing                   | Корпус                                        |
| HostelType                | Тип общежития                                 |
| Hostel                    | Общежитие                                     |
| HouseNumberType           | Тип номера дома                               |
| HouseNumber               | Номер дома                                    |
| HouseNumberAdditionally   | Дополнительный номер дома                     |
| SectionType               | Тип секции                                    |
| Section                   | Секция                                        |
| ApartmentType             | Тип квартиры                                  |
| Apartment                 | Квартира                                      |
| RoomType                  | Тип комнаты                                   |
| Room                      | Комната                                       |
| Sector                    | Сектор                                        |
| EntranceType              | Тип подъезда                                  |
| Entrance                  | Номер подъезда                                |
| FloorType                 | Тип этажа                                     |
| Floor                     | Этаж                                          |
| PostCode                  | Индекс                                        |
| Manually                  | Набор типов для дальнейшей разборки адреса    |
| NotAddress                | Не адрес                                      |
| Comment                   | Комментарий                                   |
| AdditionalData            | Дополнительные данные                         |

# Графики
## Bpemb
![accuracy](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/accuracy.png?raw=true)
![loss](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/loss.png?raw=true)
