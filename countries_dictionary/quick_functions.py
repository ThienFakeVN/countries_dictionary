from countries_dictionary import COUNTRIES
from countries_dictionary.russia import RUSSIA
from countries_dictionary.united_states import UNITED_STATES
from countries_dictionary.vietnam import VIETNAM
from json import dumps

def quick_function(dictionary: str = "countries", addition: str = ""):
    """Returns one of the dictionaries depends on the `dictionary` parameter and modify it depends on the `addition` parameter."""
    match dictionary.casefold():
        case "countries": thanhbinh = COUNTRIES
        case "russia": thanhbinh = RUSSIA
        case "united states" | "america": thanhbinh = UNITED_STATES
        case "vietnam": thanhbinh = VIETNAM
        case _: raise Exception("This dictionary does not exist (yet)")
    match addition.casefold():
        case "population density":
            for x in thanhbinh:
                if thanhbinh == COUNTRIES: thanhbinh[x]["population density"] = COUNTRIES[x]["population"] / COUNTRIES[x]["land area"]
                else: thanhbinh[x]["population density"] = thanhbinh[x]["population"] / thanhbinh[x]["area"]
        case "GDP per capita": # Issue
            if thanhbinh == COUNTRIES:
                for x in thanhbinh: thanhbinh[x]["GDP per capita"] = COUNTRIES[x]["nominal GDP"] / COUNTRIES[x]["population"]
            else: raise Exception("Only works with the Countries dictionary")
        case "ISO 3166-2": # Issue
            if thanhbinh == COUNTRIES:
                for x in thanhbinh: thanhbinh[x]["ISO 3166-2"] = "ISO 3166-2:" + COUNTRIES[x]["ISO 3166-1"]["alpha-2"]
            else: raise Exception("Only works with the Countries dictionary")
    return thanhbinh

def json_dictionary(dictionary: str = "countries", addition: str = "", indent: int | str | None = None): # Issue
    """Converts a dictionary into a JSON string"""
    thanhbinh = quick_function(dictionary, addition)
    return dumps(thanhbinh, indent=indent)

def sort_dictionary(chosen_key: str, dictionary: str = "countries", addition: str = "", reverse: bool = True):
    """Sorts a dictionary by a sortable key"""
    x = quick_function(dictionary, addition)
    y = list(x.items())
    z = []
    for t in y:
        if t[1][chosen_key] != None: z.append(t)
    thanhbinh = dict(z)
    return dict(sorted(thanhbinh.items(), key=lambda item: item[1][chosen_key], reverse=reverse))

#def filtered_dictionary(chosen_key: str, chosen_value: int | str, dictionary="countries"):
#    """Filters the chosen dictionary by a key"""
#    x = chosen_dictionary(dictionary)
#    if chosen_key == "continents" or chosen_key == "official languages":
#        return dict(filter(lambda item: chosen_value in item[1][chosen_key], x.items()))
#    else: return dict(filter(lambda item: item[1][chosen_key] == chosen_value, x.items()))
# This is still under development

# Fun functions, for entertainment purposes only (moving to quick_function()!)

#def countries_france_censored():
#    """Returns the countries dictionary with the `France` key gets censored `Fr*nce`
#
#    (This is just a joke, I don't support hate against France and French people)"""
#    new_countries = COUNTRIES
#    new_countries["Fr*nce"] = new_countries.pop("France")
#    new_countries = dict(sorted(new_countries.items()))
#    return new_countries

#def countries_allahu_akbar():
#    """Returns the countries dictionary without most countries except the two countries whose mottos are "God is the Greatest". اَللَّٰهُ أَكْبَرُ!
#
#    (I'm not a Muslim, and this is just a joke, I don't support hate against Islam and these two countries)"""
#    return dict(filter(lambda item: item[1]["motto"] == "God is the Greatest", COUNTRIES.items()))

#print(j:=json_dictionary(addition="GDP per capita", indent=4))

#with open("test.json", "w") as f: f.write(j)

population_density = quick_function(addition="population density")
gdp_per_capital = quick_function(addition="GDP per capita")
iso = quick_function(addition="ISO 3166-2")
print(gdp_per_capital)
#full_dictionary = COUNTRIES
#for x in COUNTRIES:
#    full_dictionary[x]["population density"] = population_density[x]["population density"]
#    full_dictionary[x]["GDP per capita"] = gdp_per_capital[x]["GDP per capita"]
#    full_dictionary[x]["ISO 3166-2"] = iso[x]["ISO 3166-2"]

#print(full_dictionary)