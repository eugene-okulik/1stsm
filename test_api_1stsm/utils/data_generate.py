import faker


fake = faker.Faker()


def make_body():
    return {
        "name": fake.name(),
        "data": {
            "color": fake.color_name(),
            "size": fake.random_element(elements=("small", "medium", "large"))
        }
    }
