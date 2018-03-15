
def num_to_english(N):

    teen_indices = list(range(11, 20))
    ones = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine", "ten"]
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    teen_dict = dict(zip(teen_indices, teens))
    tens = ["twenty", "thirty", "fourty", "fifty",
            "sixty", "seventy", "eighty", 'ninety']

    if N <= 10:
        return ones[N]
    elif N > 10 and N < 20:
        return teen_dict[N]
    elif N >= 20 and N < 100:
        tens_spot = N // 10
        one_spot = N % 10

        if N % 10 == 0:

            return tens[tens_spot - 2]
        else:
            return tens[tens_spot - 2] + " " + ones[one_spot]
    else:
        return "Invalid entry"


print(num_to_english(10))
print(num_to_english(14))
print(num_to_english(24))
print(num_to_english(20))
print(num_to_english(100))


