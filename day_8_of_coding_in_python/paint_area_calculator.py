import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paints.")
    
test_h = int(input("Wall height: "))
test_w = int(input("Wall width: "))
coverage = int(input("Paint coverage: "))

paint_calc(height=test_h, width=test_w, cover=coverage)    
    
    
    