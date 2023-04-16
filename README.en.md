# UAddress - Deepparse model

Model uaddress for library [deepparse](https://github.com/GRAAL-Research/deepparse)

> Read this in other language: [English](README.en.md), [Русский](README.md), [Український](README.ua.md)

## Requirements
* python3
* deepparse
* pandas
* colored

## Install dependencies
```shell
pip3 install -r requirements.txt
```

## Prepare data
```shell
python3 pretrain.py
```

## Train model
```shell
python3 train.py
```

![train](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/train.gif?raw=true)

## Example
```shell
python3 example.py
```

![example](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/example.gif?raw=true)

## Structure
| File                          | Description                                               |
| :-------------                | :-------------                                            |
| example.py                    | Example of address parsing into types                     |
| train.py                      | Model training                                            |
| pretrain.py                   | Preparing data for model training                         |
| check_data.py                 | Data validation for model training                        |
| improver.py                   | Address improvement                                       |
| data/data.csv                 | Data for train the model                                  |
| data/test.csv                 | Data for validate the model after training                |
| data/raw.csv                  | Raw data to prepare data for model training               |
| data/uaddress.ckpt            | Model after training (bpemb)                              |
| data/uaddress_fasttext.ckpt   | Model after training (Fasttext)                           |

## Types
| Name                      | Description                                   |
| :-------------            | :-------------                                |
| Country                   | Country                                       |
| RegionType                | Type region                                   |
| Region                    | Region                                        |
| CountyType                | Type county                                   |
| County                    | County                                        |
| SubLocalityType           | Type sublocality                              |
| SubLocality               | Sublocality                                   |
| LocalityType              | Type locality                                 |
| Locality                  | Locality                                      |
| StreetType                | Type street                                   |
| Street                    | Street                                        |
| HousingType               | Type housing                                  |
| Housing                   | Housing                                       |
| HostelType                | Type hostel                                   |
| Hostel                    | Hostel                                        |
| HouseNumberType           | Type house number                             |
| HouseNumber               | Number house                                  |
| HouseNumberAdditionally   | Additional house number                       |
| SectionType               | Type section                                  |
| Section                   | Section                                       |
| ApartmentType             | Type apartment                                |
| Apartment                 | Apartment                                     |
| RoomType                  | Type room                                     |
| Room                      | Room                                          |
| Sector                    | Sector                                        |
| EntranceType              | Type entrance                                 |
| Entrance                  | Entrance                                      |
| FloorType                 | Type floor                                    |
| Floor                     | Floor                                         |
| PostCode                  | Index                                         |
| Manually                  | Kit types for further parsing address         |
| NotAddress                | Not address                                   |
| Comment                   | Comment                                       |
| AdditionalData            | Additional data                               |

# Graphics
## Bpemb
![accuracy](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/accuracy.png)
![loss](https://github.com/RapidappsIT/uaddress_deepparse/blob/master/doc/loss.png)