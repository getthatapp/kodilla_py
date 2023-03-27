from faker import Faker
fake = Faker()


class Contact:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.company}, {self.job}, {self.email}'

if __name__ == '__main__':

    contacts = []
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        company = fake.company()
        job = fake.job()
        email = fake.email()

        contact = Contact(first_name, last_name, company, job, email)
        contacts.append(contact)
        # contacts.sort(key=lambda x: x.first_name)
        contacts.sort(key=lambda x: x.last_name)

    for contact in contacts:
        print(contact)
