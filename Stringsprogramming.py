"""
From the standard input, read your country and year of birth (country, age: Hungary-1991).

Separate the scanned data at the hyphen (-).

Print the data to the standard output in the following format:

Country: Hungary

Year of birth: 1991    
"""
biodata = input("Kindly input your country, age details following the format : :Hungary-1991  ")
print(biodata.rsplit(sep='-'))
country = biodata.rsplit(sep='-')[0]
Year_of_birth = biodata.rsplit(sep='-')[1]
print('country:',country, '\nYear of birth:',1991)
