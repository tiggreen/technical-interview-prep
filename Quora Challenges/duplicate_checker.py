#!/usr/bin/env python
import sys


def check(expected, output):
    correct = {}

    expectedlines = expected.splitlines()
    outputlines = output.splitlines()

    if len(outputlines) != len(expectedlines):
        print >> sys.stderr, 'Incorrect number of rows'
        return 0.0

    num_correct = 0
    num_false_positive = 0
    num_false_negative = 0
    num_wrong = 0
    total = 0

    for l in expectedlines:
        data = l.split(' ')
        correct[(data[0], data[1])] = int(data[2])
        total += 1

    for l in outputlines:
        data = l.split(' ')
        key = (data[0], data[1])
        actual_val = int(data[2])
        expected_val = correct.get(key)

        if actual_val == expected_val:
            num_correct += 1
        elif actual_val == 0 and expected_val == 1:
            num_false_negative += 1
        elif actual_val == 1 and expected_val == 0:
            num_false_positive += 1
        else:
            num_wrong += 1

    print >> sys.stderr, 'Total:', total
    score = 1.0 * num_correct / total

    print >> sys.stderr, 'Num correct:', num_correct, '(%.2f%%)' % (100.*num_correct/total)
    print >> sys.stderr, 'Num false positive:', num_false_positive, '(%.2f%%)' % (100.*num_false_positive/total)
    print >> sys.stderr, 'Num false negative:', num_false_negative, '(%.2f%%)' % (100.*num_false_negative/total)
    print >> sys.stderr, 'Num wrong type:', num_wrong, '(%.2f%%)' % (100.*num_wrong/total)

    return score


def main():
    check(open(sys.argv[1]).read(), open(sys.argv[2]).read())


if __name__ == '__main__':
    main()
