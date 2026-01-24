from quick_functions import quick_function
from russia import RUSSIA
from united_states import UNITED_STATES
from vietnam import VIETNAM

countries = quick_function(addition="ISO 3166-2")

def iso_finder(code: str, info_included: str | None = None):
    """Returns the name of a members or observer of the United Nations and a chosen information based on the provided ISO code"""
    for x in countries:
        y = countries[x].get(info_included, "") if info_included else ""
        iso_data = countries[x]["ISO 3166-1"]
        if code in (iso_data["alpha-2"], iso_data["alpha-3"], iso_data["numeric"], countries[x]["ISO 3166-2"]): return [x, y]
    raise Exception("No United Nations' member or observer state has this code")

def iso_ru_finder(code: str, info_included: str | None = None):
    """Returns the name of a Russian federal subject and a chosen information based on the provided ISO code
    (For occupied zones in Ukraine, check the Ukraine dictionary, it isn't available yet though)"""
    for x in RUSSIA:
        y = RUSSIA[x].get(info_included, "") if info_included else ""
        if code == RUSSIA[x]["ISO 3166-2:RU"]: return [x, y]
    raise Exception("No Russian federal subject has this code")

def iso_us_finder(code: str, info_included: str | None = None):
    """Returns the name of a US state, federal district or inhabited territory and a chosen information based on the provided ISO code"""
    for x in UNITED_STATES:
        y = UNITED_STATES[x].get(info_included, "") if info_included else ""
        if code == UNITED_STATES[x]["ISO 3166-2:US"]: return [x, y]
    raise Exception("No US state, federal district or inhabited territory has this code")

def iso_vn_finder(code: str, info_included: str | None = None):
    """Returns the name of a Vietnamese province or municipality and a chosen information based on the provided ISO code"""
    for x in VIETNAM:
        y = VIETNAM[x].get(info_included, "") if info_included else ""
        if code == VIETNAM[x]["ISO 3166-2:VN"]: return [x, y]
    raise Exception("No Vietnamese province or municipality has this code")
