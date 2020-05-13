
#from soppy import soppy

"""
I have a number of domain names in two registrars - name.com and easily.co.uk
as well as AWS. Because AWS has boto and is easier to manage I want to 
pull all the DNS into AWS.  THis is the process for how.

easily.co.uk:

mikadosoftware.com
oss4gov.org
pandapa.com
paul-brian.com


https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html

This seems most relevant
I want to transfer DNS *service* as well as DNS regstration


FInd current record details

A records
AAAA records
CNAME records
MX records


"""

from pprint import pprint as pp

def step_init():
    """Get the name of the domain and source and target registrars """
    domain=soppy.input('Domain Name please')
    from_registrar=soppy.input('From Registrar please')
    to_registrar=soppy.input('To Registrar please')
    
    soppy.init(name="{}-{}-{}".format(domain, from_registrar, to_registrar))

def step_capture_whois():
    """Get the whois data currently for domain  """
    pass

def create_hosted_zone():
    import boto3
    client = boto3.client('route53')
    resp = client.list_hosted_zones()
    pp(resp)
    for d in resp['HostedZones']:
        print(d['Name'])
    

if __name__ == '__main__':
    create_hosted_zone()
    

