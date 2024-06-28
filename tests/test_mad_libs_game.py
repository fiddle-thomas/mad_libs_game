# Test cases for Mad Libs game will be written here
### Notes on Building a Test for the Mad Libs Program

1. **Define the Test Function:**
   - Create a function called `test_madlib`.

2. **Setup Mock Inputs:**
   - Use predefined values for each input required by the program.
   - Example mock inputs:
     - Adjective 1: "fun"
     - Adjective 2: "happy"
     - Noun 1: "mountain"
     - Noun 2: "beach"
     - Plural Noun 1: "horses"
     - Verb ending in 'ing' 1: "swimming"
     - Plural Noun 2: "meals"
     - Verb ending in 'ing' 2: "relaxing"
     - Noun 3: "lake"
     - Plant 1: "ivy"
     - Part of the body 1: "foot"
     - Place 1: "park"
     - Verb ending in 'ing' 3: "jogging"
     - Number 1: "8"
     - Plural Noun 3: "toys"

3. **Expected Output:**
   - Define the expected Mad Libs result based on the mock inputs.
   - Example expected output:
     ```plaintext
     A vacation is when you take a trip to some fun place with your happy family. Usually you go to some place that is near a/an mountain or up on a/an beach. A good vacation place is one where you can ride horses. I like to spend my time swimming. When parents go on a vacation, they spend their time eating three meals a day, and fathers play golf, and mothers sit around relaxing. Last summer, my little brother fell in a/an lake and got poison ivy all over his foot. My family is going to go to (the) park, and I will practice jogging. Parents need vacations more than kids because they have to work 8 hours every day all year making enough toys to pay for the vacation.
     ```

4. **Capture the Output:**
   - Use a method to capture the output of the `print` statement.
   - Example: Redirect `sys.stdout` to capture the printed output.

5. **Compare the Output:**
   - Compare the captured output with the expected Mad Libs result.
   - Use an assertion to verify that the actual output matches the expected output.

6. **Helper Functions:**
   - Create a helper function to run the Mad Libs program with the mock inputs.
   - Create a helper function to capture the printed output.

### Pseudocode Example

```plaintext
function test_madlib():
    # Step 1: Define mock inputs
    mock_inputs = [
        "fun",       # Adjective 1
        "happy",     # Adjective 2
        "mountain",  # Noun 1
        "beach",     # Noun 2
        "horses",    # Plural Noun 1
        "swimming",  # Verb ending in 'ing' 1
        "meals",     # Plural Noun 2
        "relaxing",  # Verb ending in 'ing' 2
        "lake",      # Noun 3
        "ivy",       # Plant 1
        "foot",      # Part of the body 1
        "park",      # Place 1
        "jogging",   # Verb ending in 'ing' 3
        "8",         # Number 1
        "toys"       # Plural Noun 3
    ]
    
    # Step 2: Expected output
    expected_output = """A vacation is when you take a trip to some fun place with your happy family. Usually you go to some place that is near a/an mountain or up on a/an beach. A good vacation place is one where you can ride horses. I like to spend my time swimming. When parents go on a vacation, they spend their time eating three meals a day, and fathers play golf, and mothers sit around relaxing. Last summer, my little brother fell in a/an lake and got poison ivy all over his foot. My family is going to go to (the) park, and I will practice jogging. Parents need vacations more than kids because they have to work 8 hours every day all year making enough toys to pay for the vacation."""
    
    # Step 3: Capture the output
    captured_output = capture_output(lambda: run_madlib_program(mock_inputs))
    
    # Step 4: Assert the output
    assert captured_output == expected_output, f"Test failed. Expected: {expected_output}, but got: {captured_output}"

# Helper function to run the program with mock inputs
function run_madlib_program(inputs):
    index = 0
    adj_1 = inputs[index]; index += 1
    adj_2 = inputs[index]; index += 1
    noun_1 = inputs[index]; index += 1
    noun_2 = inputs[index]; index += 1
    pl_noun_1 = inputs[index]; index += 1
    verb_ing_1 = inputs[index]; index += 1
    pl_noun_2 = inputs[index]; index += 1
    vern_ing_2 = inputs[index]; index += 1
    noun_3 = inputs[index]; index += 1
    plant_1 = inputs[index]; index += 1
    part_of_body_1 = inputs[index]; index += 1
    place_1 = inputs[index]; index += 1
    verb_ing_3 = inputs[index]; index += 1
    num_1 = inputs[index]; index += 1
    pl_noun_3 = inputs[index]; index += 1
    
    madlib = f"A vacation is when you take a trip to some {adj_1} place with your {adj_2} family. Usually you go to some place that is near a/an {noun_1} or up on a/an {noun_2}. A good vacation place is one where you can ride {pl_noun_1}. I like to spend my time {verb_ing_1}. When parents go on a vacation, they spend their time eating three {pl_noun_2} a day, and fathers play golf, and mothers sit around {vern_ing_2}. Last summer, my little brother fell in a/an {noun_3} and got poison {plant_1} all over his {part_of_body_1}. My family is going to go to (the) {place_1}, and I will practice {verb_ing_3}. Parents need vacations more than kids because they have to work {num_1} hours every day all year making enough {pl_noun_3} to pay for the vacation."
    
    print(madlib)

# Helper function to capture output
function capture_output(func):
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

# Run the test
test_madlib()
```

Use these notes to guide you through building and implementing the test for the Mad Libs program.
