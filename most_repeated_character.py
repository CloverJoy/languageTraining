from pprint import pprint
sentence = "this is a common interview question"


def most_char(sentence):
    # iterate string
    # create object for counting each characters
    # iterate find the largest character, return char
    tracker = {}
    for char in sentence:
        if char == " ":
            continue
        if char not in tracker:
            tracker[char] = 1
        tracker[char] += 1
    # pprint(tracker, width=1)
    # my solution:
    highest = 0
    result = ""
    for key in tracker:
        if (tracker[key] > highest):
            highest = tracker[key]
            result = key
    # elegant with sort and lambda
    tracker_sorted = sorted(
        tracker.items(),
        key=lambda kv: kv[1],
        reverse=True
    )
    print(tracker_sorted[0])
    return result


print(most_char(sentence))
