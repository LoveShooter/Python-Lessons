def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address,

    }
    return record

user1 = create_record("Vasya", "+97435345435", "Tunissia")
user2 = create_record("Petya", "+97466777435", "Marocco")

print(user1)
print(user2)


def give_award(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("Tovarisch " + person.title() + " nagrazhdaetsya medaliu " + medal)


give_award("Za Berlin", "vasya", "petya")
give_award("Za London", "valentin", "petya", "alexander")
