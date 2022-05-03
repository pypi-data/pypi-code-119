'''File for handling all operations relating to the HumanName datatype'''

from faker import Faker


def generateName(gender: str = 'U'):
    '''Function to generate a FHIR HumanName based on gender'''
    human_name = {
        'family': generateFamilyName(),
        'given': [generateGivenName(gender)]
    }
    return human_name


def generateFamilyName():
    '''Function to generate family name'''
    fake = Faker()
    return fake.last_name()


def generateGivenName(gender: str = 'U'):
    '''Function to generate given name'''
    fake = Faker()
    if gender == 'M':
        return fake.first_name_male()
    if gender == 'F':
        return fake.first_name_female()
    return fake.first_name_nonbinary()
