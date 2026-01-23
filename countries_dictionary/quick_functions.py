from countries_dictionary import COUNTRIES
from countries_dictionary.russia import RUSSIA
from countries_dictionary.united_states import UNITED_STATES
from countries_dictionary.vietnam import VIETNAM
from json import dumps
from copy import deepcopy

def quick_function(dictionary: str = "countries", addition: str = ""):
    """Returns one of the dictionaries depends on the `dictionary` parameter and modify it depends on the `addition` parameter."""
    match dictionary.casefold():
        case "countries": thanhbinh = deepcopy(COUNTRIES)
        case "russia": thanhbinh = deepcopy(RUSSIA)
        case "united states" | "america": thanhbinh = deepcopy(UNITED_STATES)
        case "vietnam": thanhbinh = deepcopy(VIETNAM)
        case _: raise Exception("This dictionary does not exist (yet)")
    match addition.casefold():
        case "population density":
            if dictionary.casefold() == "countries":
                for x in thanhbinh: thanhbinh[x]["population density"] = thanhbinh[x]["population"] / thanhbinh[x]["land area"]
            else:
                for x in thanhbinh: thanhbinh[x]["population density"] = thanhbinh[x]["population"] / thanhbinh[x]["area"]
        case "gdp per capita":
            if dictionary.casefold() == "countries":
                for x in thanhbinh: thanhbinh[x]["GDP per capita"] = thanhbinh[x]["nominal GDP"] / thanhbinh[x]["population"]
            else: raise Exception("Only works with the Countries dictionary")
        case "iso 3166-2":
            if dictionary.casefold() == "countries":
                for x in thanhbinh: thanhbinh[x]["ISO 3166-2"] = "ISO 3166-2:" + thanhbinh[x]["ISO 3166-1"]["alpha-2"]
            else: raise Exception("Only works with the Countries dictionary")
    return thanhbinh

def json_dictionary(dictionary: str = "countries", addition: str = "", indent: int | str | None = None):
    """Converts a dictionary into a JSON string"""
    thanhbinh = quick_function(dictionary, addition)
    return dumps(thanhbinh, indent=indent)

def sort_dictionary(chosen_key: str, dictionary: str = "countries", addition: str = "", reverse: bool = True):
    """Sorts a dictionary by a sortable key"""
    x = quick_function(dictionary, addition)
    y = list(x.items())
    z = []
    for t in y:
        if t[1][chosen_key] is not None: z.append(t)
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
