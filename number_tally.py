def number_tally(numbers):
    tally = {}
    
    for number in numbers:
        if number not in tally:
            tally[number]=0
        tally[number]+= 1
    print (tally)
    return tally
    
numbers = "123475661264"
number_tally(numbers)