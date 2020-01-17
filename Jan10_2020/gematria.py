ones = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
tens = ["ZERO", "TEN_shouldn't use", "TWENTY", "THIRTY", "FOURTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]

hundred = "HUNDRED"
thousand = "THOUSAND"

million = "MILLION"
billion = "BILLION"
trillion = "TRILLION"




def three_digit_to_str(Tnum):

    num = Tnum
    retStr = ""

    if num >= 100:
        hund = num / 100
        retStr += ones[hund]
        retStr += hundred
        num = num % 100

    if num >= 20:
        ten = num / 10
        retStr += tens[ten]
        num = num % 10

    if num >= 10:
        teen = num - 10
        retStr += teens[teen]
        num = 0

    if num > 0:
        retStr += ones[num]

    return retStr


def construct_word(wholeNum):

    num = wholeNum
    retStr = ""

    if num >= (1000 * 1000):
        retStr += three_digit_to_str(num/(1000*1000))
        retStr += million
        num = num % (1000 * 1000)


    if num >= (1000):
        retStr += three_digit_to_str(num/1000)
        retStr += thousand
        num = num % 1000

    if num > (0):
        retStr += three_digit_to_str(num)

    return retStr


def calc_gem_val(word):

    val = 0

    for c in word:

        if c != ' ':

            val += (ord(c) - ord("A")) + 1

    return val


def main():

    print "value : char sum : word"

    for i in range(10):

        s = construct_word(i)
        val = calc_gem_val(s)
        if True: #val:
            print "{0} : {1} : {2}".format(i, val, s)

main()
