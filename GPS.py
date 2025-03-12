location = [("Berlin", (40.7128, -74.0060)),
            ("Hamburg", (34.0522, -118.2437)),
            ("Munich", (41.8781, -87.6298)),]

def get_location(city):
    for for_name, word in location:
        if city == for_name:
            return word
        
        city = "Berlin"
        coordinate = get_location(city)

        if coordinate:
            print(f"The coordinate of {city} is {coordinate}")
        else:
            print(f"Location for {city} not found.")