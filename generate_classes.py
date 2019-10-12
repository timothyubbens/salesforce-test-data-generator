from simple_salesforce import Salesforce
import pprint
import json

username = ''
password = ''
security_token = ''
object_name = 'Contact'

sf = Salesforce(username, password, security_token)

# Describe object
object_describe = eval('sf.'+object_name+'.describe()')

field_names_string = ''
field_names = []
field_dict = {}
for obj_describe_field in object_describe.get('fields'):
    if(obj_describe_field.get('createable')):
        field_name = obj_describe_field.get('name')
        field_names_string += ',\n      ' + field_name
        field_names.append(field_name)

        # determine faker to use
        field_type = obj_describe_field.get('type')
        if field_type == 'picklist':
            # generate picklist val string
            picklist_vals = []
            for pick_val in obj_describe_field.get('picklistValues'):
                if pick_val.get('active'):
                    picklist_vals.append('\'{}\''.format(pick_val.get('value')))
            field_dict[field_name] = 'factory.Faker(\'word\', ext_word_list=[{}])'.format(', '.join(picklist_vals))
        elif field_type == 'boolean':
            field_dict[field_name] = 'factory.Faker(\'boolean\', chance_of_getting_true=50)'
        elif field_type == 'date':
            field_dict[field_name] = 'factory.Faker(\'date\', pattern="%Y-%m-%d", end_datetime=None)'
        elif field_type == 'datetime':
            field_dict[field_name] = 'factory.Faker(\'iso8601\', tzinfo=None, end_datetime=None)'
        elif field_type == 'phone':
            field_dict[field_name] = 'factory.Faker(\'phone_number\')'
        elif field_type == 'email':
            field_dict[field_name] = 'factory.Faker(\'ascii_safe_email\')'
        else: 
            field_dict[field_name] = 'factory.Faker(\'\')'

# Output generated class
classpath = './factories/{}.py'.format(object_name)
classfile = open(classpath, 'w')

classfile.write('import factory\n\n')
classfile.write('class {}(object):\n'.format(object_name))
classfile.write('    def __init__(self{}):\n'.format(field_names_string))
for field_name in field_names:
    classfile.write('        self.{} = {}\n'.format(field_name, field_name))
classfile.write('\n')
classfile.write('class {}Factory(factory.Factory):\n'.format(object_name))
classfile.write('    class Meta:\n')
classfile.write('        model = {}\n\n'.format(object_name))
for field_name in field_names:
    classfile.write('    {} = {}\n'.format(field_name, field_dict[field_name]))
