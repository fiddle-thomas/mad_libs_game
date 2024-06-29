
def test_madlib():
   mock_inputs = [ 
      "fun", # adj_1 
      "happy", # adj_2
      "mountain", # noun_1
      "beach", # noun_2
      "horses", # pl_noun_1
      "swimming", # verb_ing_1
      "meals", # pl_noun_2
      "relaxing", # verb_ing_2
      "lake", # noun_3
      "ivy", # plant_1
      "foot", # part_of_body_1
      "park", # place_1
      "jogging", # verb_ing_3
      "8", # num_1
      "toys", # pl_noun_3
   ]

expected_output = "A vacation is when you take a trip to some fun place with your happy family. Usually you go to some place that is near a/an mountain or up on a/an beach. A good vacation place is one where you can ride horses. I like to spend my time swimming. When parents go on a vacation, they spend their time eating three meals a day, and fathers play golf, and mothers sit around relaxing. Last summer, my little brother fell in a/an lake and got poison ivy all over his foot. My family is going to go to (the) park, and I will practice jogging. Parents need vacations more than kids because they have to work 8 hours every day all year making enough toys to pay for the vacation."
