import factory

class Contact(object):
    def __init__(self,
      LastName,
      FirstName,
      Salutation,
      Phone,
      Email,
      Birthdate,
      DoNotCall,
      EmailBouncedDate):
        self.LastName = LastName
        self.FirstName = FirstName
        self.Salutation = Salutation
        self.Phone = Phone
        self.Email = Email
        self.Birthdate = Birthdate
        self.DoNotCall = DoNotCall
        self.EmailBouncedDate = EmailBouncedDate

class ContactFactory(factory.Factory):
    class Meta:
        model = Contact

    LastName = factory.Faker('last_name')
    FirstName = factory.Faker('first_name')
    Salutation = factory.Faker('word', ext_word_list=['Mr.', 'Ms.', 'Mrs.', 'Dr.', 'Prof.'])
    Phone = factory.Faker('phone_number')
    Email = factory.Faker('ascii_safe_email')
    Birthdate = factory.Faker('date', pattern="%Y-%m-%d", end_datetime=None)
    DoNotCall = factory.Faker('boolean', chance_of_getting_true=50)
    EmailBouncedDate = factory.Faker('iso8601', tzinfo=None, end_datetime=None)
