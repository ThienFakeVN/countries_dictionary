"""A Python module for dictionaries of countries and related functions"""

__author__ = "Ngô Trần Quang Thiện"
__email__ = "quangthienngotran@gmail.com"
__version__ = "8.1.0"

from .countries import COUNTRIES
from .russia import RUSSIA
from .united_states import UNITED_STATES
from .vietnam import VIETNAM

from .unrecognised_states import UNRECOGNISED_STATES
from .unrecognised_states.transnistria import TRANSNISTRIA

from .tools.quick_functions import quick_function, json_dictionary, sort_dictionary
from .tools.iso_finder import iso_finder, iso_ru_finder, iso_us_finder, iso_vn_finder
