# Communist states dictionary
The communist states dictionary, consists of all existing communist states and their information.

## Structure
Each key in the `COMMUNIST_STATES` constant has 10 items:
```py
COMMUNIST_STATES = {
    "China": {
        "party": "Communist Party of China",
        "politburo seats": 23,
        "politburo's term": 20,
        "central committee's members": 205,
        "central committee's alternates": 171,
        "central committee's term": 20,
        "SSOP": "National People's Congress",
        "SSOP seats": 2977, # Excluding NPCSC
        "party's SSOP seats": 2040, # Excluding NPCSC
        "SSOP's term": 14,
    },
    # ...
}
```

- `"party"`: Ruling communist party of the country, type: `str`

- `"politburo seats"`: Number of seats in the ruling communist party's politburo, type: `int`

- `"politburo's term"`: Current term of the politburo, type: `int`

- `"central committee's members"`: Number of members of the ruling communist party's central committee, type: `int`

- `"central committee's alternates"`: Number of alternates of the central committee, type: `int`

- `"central committee's term"`: Current term of the central committee, type: `int`

- `"SSOP"`: Name of the country's supreme state organ of power (i.e. parliament), type: `str`

- `"SSOP seats"`: Number of total seats in the supreme state organ of power, type: `int`

- `"party's SSOP seats"`: Number of seats in the supreme state organ of power the ruling communist party holds, type: `int`

- `"SSOP's term"`: Current term of the supreme state organ of power, type: `int`

## Usage example
```py
from countries_dictionary import COMMUNIST_STATES

# Prints the name of the ruling communist party of a country
print(COMMUNIST_STATES["Vietnam"]["party"])

# Compare the current SSOP's term of two countries
print(COMMUNIST_STATES["Cuba"]["SSOP's term"] > COMMUNIST_STATES["Laos"]["SSOP's term"])
print(COMMUNIST_STATES["Cuba"]["SSOP's term"] == COMMUNIST_STATES["Laos"]["SSOP's term"])
print(COMMUNIST_STATES["Cuba"]["SSOP's term"] < COMMUNIST_STATES["Laos"]["SSOP's term"])

# Create the list of all communist states
list_of_communist_states = list(COMMUNIST_STATES.keys())
print(list_of_communist_states)
```
