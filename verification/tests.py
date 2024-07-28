"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        [
    {
        "input": [{'maçã': 10, 'banana': 5}, {'maçã': 3, 'laranja': 7}],
        "answer": {'maçã': 13, 'banana': 5, 'laranja': 7}
    },
    {
        "input": [{'pêra': 5}, {'pêra': 5, 'uva': 2}],
        "answer": {'pêra': 10, 'uva': 2}
    }
]
    ]
}
