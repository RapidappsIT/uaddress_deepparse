import re

##
# IMPROVE ADDRESS
#
def improve_address(address):
    address = re.sub(r'(?!^)(\,)(?!\s)(?!$)', ', ', address)
    address = re.sub(r'\;', '', address)
    address = re.sub(r'\s\,', ',', address)
    address = re.sub(r'\s+', ' ', address)
    address = re.sub(r'^\s+|\s+$', '', address)
    address = re.sub(r'\s\.', '.', address)
    address = re.sub(r'\s\,', ',', address)
    address = re.sub(r'\s\-\,|\,\s\-\s', '', address)
    address = re.sub(r'\,$|^\,\s', '', address)
    address = re.sub(r'[\’\`\”\'“\"_]', '’', address)
    address = re.sub(r'\’{2}', '’', address)
    address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐ.])\’(?![a-zA-Zа-яА-ЯіІїЇґҐ])', '', address)
    address = re.sub(r'(?<=\d)\/(?=[a-zA-Zа-яА-ЯіІїЇґҐ]{3,})', '/ ', address)
    address = re.sub(r'(?<=\d{5})(?=[a-zA-Zа-яА-ЯіІїЇґҐ.])', ' ', address)

    address = fixString(address)

    return address
##
# FIX STRING
#
def fixString(address):

    ##
    # Unmerge string, if exists housenumber + apartment type
    #
    if re.findall(r'\d{1,}[a-zA-Zа-яА-ЯіІїЇґҐ]{1}[a-zA-Zа-яА-ЯіІїЇґҐ]{1}\s', address):
        address = re.sub(r'(?<=\d)(?=[a-zA-Zа-яА-ЯіІїЇґҐ]+\s)', ' ', address)

    if re.findall(r'кв\s\d+$', address):
        address = re.sub(r'(?=кв(?:\.|\.?)\s\d+)', ' ', address)
    
    if re.findall(r'(?<=\d[a-zA-Zа-яА-ЯіІїЇґҐ]{1})(?=[a-zA-Zа-яА-ЯіІїЇґҐ]\.\d\s)', address):
        address = re.sub(r'(?<=\d[a-zA-Zа-яА-ЯіІїЇґҐ]{1})(?=[a-zA-Zа-яА-ЯіІїЇґҐ]\.\d\s)', ' ', address)

    if re.findall(r'(?<=\d)(?=[a-zA-Zа-яА-ЯіІїЇґҐ]{3,}(?:\s|\.\d+$))', address):
        address = re.sub(r'(?<=\d)(?=[a-zA-Zа-яА-ЯіІїЇґҐ]{3,}(?:\s|\.\d+$))', ' ', address)

    if re.findall(r'\d+[a-zA-Zа-яА-ЯіІїЇґҐ]\.\d+', address):
        address = re.sub(r'(?<=\d)(?=[a-zA-Zа-яА-ЯіІїЇґҐ]\.\d+)', ' ', address)

    if re.findall(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐ]\.)(?=\d+(?:\s|\,))', address):
        address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐ]\.)(?=\d+(?:\s|\,))', ' ', address)

    if re.findall(r'[a-zA-Zа-яА-ЯіІїЇґҐ]{1,}\s[a-zA-Zа-яА-ЯіІїЇґҐ]{1,}\d\s', address):
        address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐ])(?=\d\s)', ' ', address)

    if re.findall(r'\.\(', address):
        address = re.sub(r'\.\(', '. (', address)

    ##
    # ADDING SPACE BEFORE BRACKET
    #
    if re.findall(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐ])\(', address):
        address = re.sub(r'(?<=[a-zA-Zа-яА-ЯіІїЇґҐ])\(', ' (', address)

    ##
    # REMOVE SPACE AFTER HYPHEN
    #
    if re.findall(r'\s+\-\s+|\-\s+', address):
        address = re.sub('\s+\-\s+|\-\s+', '-', address)

    return address