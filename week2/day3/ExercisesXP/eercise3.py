# if
brand = "b"
b = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

b["numbers_stores"] = 2
b["country_creation"] = "Spain"

if "international_competitors" in b:
    b["international_competitors"].append("Desigual")

print(b["international_competitors"][-1])

print(b["major_color"]["US"])

print(len(b))

print(b.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

print(b["number_stores"])
