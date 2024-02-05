
**Pokemon API Test Script**


This script uses pytest for testing and requests library to interact with the Pokemon API.

**Prerequisites**
Python 3.x
pytest (pip install pytest)
requests (pip install requests)


**Usage**
Clone the repository or download the script. Copy code-
`git clone https://github.com/Or-Shamir/-matrix.git`
`cd your_repository`

Install the required packages-
`pip install -r requirements.txt`

Run the script.
`python Pokemon_poc.py`

View the test results.


**Structure**
Pokemon_poc.py: The main Python script containing the test functions.
requirements.txt: A file containing the required Python packages.


**Test Functions**
1. _test_pokemon_type_api_response()_
    * Verifies the response from the Pokemon API for the types of Pokemon.
    * Checks if the response is a dictionary in JSON format.
    * Ensures there are exactly 20 different Pokémon types.
2. _test_fire_type_pokemon()_
    * Builds on the previous test by querying the 'fire' type Pokemon.
    * Validates the presence of 'charmander' in the list.
    * Validates the absence of 'bulbasaur' in the list.
3. _test_heaviest_fire_type_pokemon()_
    * Extends the previous tests to find the 5 heaviest 'fire' type Pokemon.
    * Compares the result with an expected dictionary of heaviest Pokemon and prints the result.


**Running the Tests**
Execute the script with pytest:
`pytest -v Pokemon_poc.py`
The -v flag stands for verbose, providing detailed information about the tests being run.
