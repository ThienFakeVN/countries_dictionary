from countries_dictionary.quick_function import quick_function
from countries_dictionary.russia import RUSSIA
from countries_dictionary.united_states import UNITED_STATES
from countries_dictionary.vietnam import VIETNAM

def iso_finder(code: str, info_included: str = None, dictionary="countries"):
    """Returns the name of the country/federal subject/state/province and its chosen information based on the provided ISO code"""
    dictionary = quick_function(dictionary, "ISO 3166-2")
    for x in dictionary:
        y = dictionary[x].get(info_included, "") if info_included else ""
        iso_data = dictionary[x]["ISO 3166-1"]
        if code in (iso_data["alpha-2"], iso_data["alpha-3"], iso_data["numeric"], dictionary[x]["ISO 3166-2"]): return [x, y]
    raise Exception("No country/federal subject/state/province has this code")
