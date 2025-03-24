import geocoder

def get_location():
    try:
        location = geocoder.ip('me')
        if location.latlng:
            print(f"Your Current Location: {location.city}, {location.country}")
            return location.city, location.country
        else:
            print("Could not detect location.")
            return None, None
    except Exception as e:
        print(f"Error getting location: {e}")
        return None, None

if __name__ == "__main__":
    city, country = get_location()
    if city and country:
        print(f"Detected Location: {city}, {country}")