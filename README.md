# Salesforce Data Generator

A simple Salesforce data generator and a utility to generate the base of the factory for each class.

Build factories:
1. Add user credentials to `generate_classes.py`
1. Set `object_name` in `generate_classes.py` to the object you'd like to generate a factory for
1. Run `python generate_classes.py`
1. Update the resultant factory in `factories/` with additional data fakers.  See [https://faker.readthedocs.io/] for options.  Sample Contact factory included.

Insert records using the factories:
1. Use a python script similar to `generate_records.py` to generate records using the factories you've built