from countries_dictionary.quick_functions import countries_iso_3166_2

countries = countries_iso_3166_2()

def iso_finder(code: str, formal_name_included = False):
    """Returns the name of the country based on the provided ISO code"""
    for x in countries:
        if formal_name_included == True: formal_name = f" — {countries[x]["formal name"]}"
        else: formal_name = ""
        if code == countries[x]["ISO 3166-1"]["alpha-2"]: return x + formal_name
        else:
            if code == countries[x]["ISO 3166-1"]["alpha-3"]: return x + formal_name
            else:
                if code == countries[x]["ISO 3166-1"]["numeric"]: return x + formal_name
                else:
                    if code == countries[x]["ISO 3166-2"]: return x + formal_name
    raise Exception("No United Nations' member or observer state has this code")