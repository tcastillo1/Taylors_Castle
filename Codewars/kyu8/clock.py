# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s):
    # return (h * 60 * 60 * 1000) + (m * 60 * 1000) + (s * 1000)
    print(1000*((h * 60 * 60) + (m * 60) + (s)))


past(1, 30, 20)
