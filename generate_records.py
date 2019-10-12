from simple_salesforce import Salesforce
from factories.Contact import ContactFactory
import factory

sf = Salesforce(username='', password='', security_token='')

for i in range(3):
    record = factory.build(dict, FACTORY_CLASS=ContactFactory)
    sf.Contact.create(record)
