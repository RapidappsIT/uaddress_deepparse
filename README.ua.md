# UAddress - Deepparse model

Модель uaddress для бібліотеки [deepparse](https://github.com/GRAAL-Research/deepparse)

> Read this in other language: [English](README.en.md), [Русский](README.md), [Український](README.ua.md)

## Вимоги
* python3
* deepparse
* pandas
* colored

## Встановлення залежностей
```shell
pip3 install -r requirements.txt
```

## Підготовка данних
```shell
python3 pretrain.py
```

## Навчання моделі
```shell
python3 train.py
```

![train](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/train.gif?raw=true)

## Приклад
```shell
python3 example.py
```

![example](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/example.gif?raw=true)

## Структура
| Файл                          | Опис                                                      |
| :-------------                | :-------------                                            |
| example.py                    | Приклад розбирання адреси на типи                         |
| train.py                      | Навчання моделі                                           |
| pretrain.py                   | Підготовка даних для навчання моделі                      |
| check_data.py                 | Перевірка даних для навчання моделі                       |
| improver.py                   | Удосконалення адреси                                      |
| data/data.csv                 | Дані для навчання моделі                                  |
| data/test.csv                 | Дані для перевірки моделі після навчання                  |
| data/raw.csv                  | Сирі дані для підготовки даних для навчання моделі        |
| data/uaddress.ckpt            | Модель після навчання (bpemb)                             |
| data/uaddress_fasttext.ckpt   | Модель після навчання (Fasttext)                          |

## Типи
| Назва                     | Опис                                          |
| :-------------            | :-------------                                |
| Country                   | Країна                                        |
| RegionType                | Тип області                                   |
| Region                    | Область                                       |
| CountyType                | Тип району                                    |
| County                    | Район                                         |
| SubLocalityType           | Тип підрайону                                 |
| SubLocality               | Підрайон                                      |
| LocalityType              | Тип населеного пункту                         |
| Locality                  | Населений пункт                               |
| StreetType                | Тип вулиці                                    |
| Street                    | Вулиця                                        |
| HousingType               | Тип корпусу                                   |
| Housing                   | Корпус                                        |
| HostelType                | Тип гуртожитку                                |
| Hostel                    | Гуртожиток                                    |
| HouseNumberType           | Тип номеру будинку                            |
| HouseNumber               | Номер будинку                                 |
| HouseNumberAdditionally   | Додатковий номер будинку                      |
| SectionType               | Тип секції                                    |
| Section                   | Секція                                        |
| ApartmentType             | Тип квартири                                  |
| Apartment                 | Квартира                                      |
| RoomType                  | Тип кімнати                                   |
| Room                      | Кімната                                       |
| Sector                    | Сектор                                        |
| EntranceType              | Тип під'їзду                                  |
| Entrance                  | Номер під'їзду                                |
| FloorType                 | Тип поверху                                   |
| Floor                     | Поверх                                        |
| PostCode                  | Індекс                                        |
| Manually                  | Набір типів для подальшого розбирання адреси  |
| NotAddress                | Не адреса                                     |
| Comment                   | Коментар                                      |
| AdditionalData            | Додаткові дані                                |

# Графіки
## Bpemb
![accuracy_bpemb](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/accuracy_bpemb.png?raw=true)
![loss_bpemb](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/loss_bpemb.png?raw=true)

## Fasttext
![accuracy_fasttext](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/accuracy_fasttext.png?raw=true)
![loss_fasttext](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/loss_fasttext.png?raw=true)