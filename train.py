import os
from deepparse.dataset_container import CSVDatasetContainer
from deepparse.parser import AddressParser

os.system('rm -rf checkpoints')
os.system('clear')

print("#" * 50)
print("# Model training ...")
print("#" * 50)

saving_dir = "./data"
file_extension = "csv"
training_dataset_name = "data"
test_dataset_name = "test"

training_container = CSVDatasetContainer(
    os.path.join(saving_dir, training_dataset_name + "." + file_extension),
    column_names=["Address", "Tags"],
    separator=";",
)

test_container = CSVDatasetContainer(
    os.path.join(saving_dir, test_dataset_name + "." + file_extension),
    column_names=["Address", "Tags"],
    separator=";",
)

tag_dictionary = {
    'Country': 0,
    'RegionType': 1,
    'Region': 2,
    'CountyType': 3,
    'County': 4,
    'SubLocalityType': 5,
    'SubLocality': 6,
    'LocalityType': 7,
    'Locality': 8,
    'StreetType': 9,
    'Street': 10,
    'HousingType': 11,
    'Housing': 12,
    'HostelType': 13,
    'Hostel': 14,
    'HouseNumberType': 15,
    'HouseNumber': 16,
    'HouseNumberAdditionally': 17,
    'SectionType': 18,
    'Section': 19,
    'ApartmentType': 20,
    'Apartment': 21,
    'RoomType': 22,
    'Room': 23,
    'Sector': 24,
    'EntranceType': 25,
    'Entrance': 26,
    'FloorType': 27,
    'Floor': 28,
    'PostCode': 29,
    'Manually': 30,
    'NotAddress': 31,
    'Comment': 32,
    'AdditionalData': 33,
    'EOS': 34
}

address_parser = AddressParser(
    model_type="bpemb",
    device=0,
    attention_mechanism=True
)

address_parser.retrain(
    training_container,
    train_ratio=0.8,
    epochs=150,
    batch_size=16,
    num_workers=2,
    prediction_tags=tag_dictionary
)

address_parser.test(test_container, batch_size=256)

os.system('cp checkpoints/retrained_bpemb_attention_address_parser.ckpt data/uaddress.ckpt')