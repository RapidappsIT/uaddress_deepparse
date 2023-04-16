from deepparse.parser import AddressParser
import improver
import os

os.system('clear')

print("#" * 50)
print("# Address parsing ...")
print("#" * 50)

address_parser = AddressParser(
    device=0,
    model_type="bpemb", 
    attention_mechanism=True,
    path_to_retrained_model="./data/uaddress.ckpt"
)

while True:
    address = input("Enter address: ")

    parse = address_parser(
        improver.improve_address(address)
    )

    parsed = parse.to_dict()
    print(parse)

    print("#" * 67)
    print("# {!s:30} | {!s:30} #".format('Label', 'String'))
    print("#" * 67)

    for label, str in parsed.items():

        print("| {!s:30} | {!s:30} |".format(label, str))

    print("#" * 67)

        
