def PatternCount(text, pattern):
    """
    Input: Strings Text and Pattern.
    Output: Count(Text, Pattern).
    Counts no. of occurrences of pattern
    """
    count = 0
    len_p = len(pattern)
    for i in range(len(text) - len_p):
        if text[i:i + len_p] == pattern:
            count += 1
    return count


def FrequentWords(text, k):
    """
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.
     Returns most frequent words
    """
    c_dict = {}  # Contains pattern as key and its count as value
    freqPatts = []  # Stores most frequent pattern(s)
    maxCount = 0  # Stores count of most frequent pattern(s)
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        if pattern not in c_dict:
            c_dict[pattern] = 1
        else:
            c_dict[pattern] += 1
            currCount = c_dict[pattern]  # Stores count of the current pattern
            if currCount >= maxCount:
                if currCount == maxCount:
                    freqPatts.append(pattern)
                else:
                    freqPatts = [pattern]
                    maxCount = currCount
    return " ".join(sorted(freqPatts))

def FrequentWordsFile(filename):
    """
     FrequentWords with file I/O
    """
    with open(filename) as file:
        text = file.readline()
        k = int(file.readline())
    result = FrequentWords(text, k)
    with open('output.txt', 'w+') as fh:
        fh.write(result)
    print('Result written to file output.txt')


def ReverseComp(text):
    my_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    result = ''
    for letter in text:
        result += my_dict[letter]
    return result[::-1]


def FindStart(text, pattern):
    len_p = len(pattern)
    result = ''
    for i in range(len(text)-len_p+1):
        if text[i:i + len_p] == pattern:
            result += (str(i) + ' ')
    return result


def FindStartFile(filename):  # With file I/O
    with open(filename) as file:
        pattern = file.readline().rstrip('\n')
        text = file.readline()
    result = FindStart(text, pattern)
    with open('output.txt', 'w+') as fh:
        fh.write(result)
    print('Result written to file output.txt')


def ClumpFinder(text, k, L, t):
    """
    Clump Finding Problem: Find patterns forming clumps in a string.
    Input: A string Genome, and integers k, L, and t.
    Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """
    patDict = {}
    repeats = []  # Contains patterns with >=t occurrences
    resultList = []  # Contains patterns that form clumps
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        if pattern not in patDict:
            patDict[pattern] = [1, [i]]    # dict keys are of format [count, list of pattern starting positions]
        else:
            patDict[pattern][0] += 1
            patDict[pattern][1].append(i)
            if patDict[pattern][0] == t:
                repeats.append(pattern)
    for x in repeats:
        posList = patDict[x][1]
        for y in range(len(posList)-t+1):   # Checks if pattern repeats >= t times in a clump of length L
            if posList[y]+L >= posList[y+t-1]+k:
                resultList.append(x)
                break
    return ' '.join(sorted(resultList))


def ClumpFinderFile(filename):
    """
    ClumpFinder with file I/O
    """
    with open(filename) as file:
        text = file.readline().rstrip('\n')
        k, L, t = file.readline().split()
    result = ClumpFinder(text, int(k), int(L), int(t))
    with open('output.txt', 'w+') as fh:
        fh.write(result)
    print('Result written to file output.txt')


def SymbolToNumber(symbol):  # Helper for PatternToNumber
    my_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    try:
        return my_dict[symbol]
    except KeyError:
        print(f'{symbol} is not a valid character.')


def PatternToNumber(pattern):
    """
    Input: A DNA string Pattern.
    Output: The integer PatternToNumber(Pattern).
    """
    if not pattern:  # If pattern is empty string
        return 0
    return 4 * PatternToNumber(pattern[:-1]) + SymbolToNumber(pattern[-1])


def PatterntoNumber2(pattern):
    """
    Alternate solution.
    Works by considering pattern as a number of base 4 and converting it into decimal.
    """
    return sum((SymbolToNumber(currSymbol) * 4**(len(pattern)-1-i)) for i, currSymbol in enumerate(pattern))
    # result, len_p = 0, len(pattern)
    # for i, symbol in enumerate(pattern):
    #     result += SymbolToNumber(symbol) * 4**(len_p-1-i)
    # return result


def ComputingFrequencies(text, k):
    """
    Returns frequency array.
    Input: A DNA string Text followed by an integer k.
    Output: FrequencyArray(Text).
    """
    freqArray = [0] * 4**k
    for i in range(len(text) - k + 1):
        freqArray[PatternToNumber(text[i:i + k])] += 1
    return ' '.join(map(str, freqArray))


def ComputingFrequenciesFile(filename):
    with open(filename) as file:
        text = file.readline().rstrip('\n')
        k = int(file.readline())
    result = ComputingFrequencies(text, k)
    with open('output.txt', 'w+') as fh:
        fh.write(result)
    print('Result written to file output.txt')


def NumberToSymbol(num):
    my_dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    try:
        return my_dict[num]
    except KeyError:
        print(f'{num} is not a valid input.')


def NumberToPattern(num, k):
    # Iterative
    q = num // 4
    r = num % 4
    result = ''
    while not (r == 0 and q == 0):
        result += NumberToSymbol(r)
        r = q % 4
        q = q // 4
    return result[::-1].rjust(k, 'A')


def NumberToPattern2(num, k):
    # Recursive
    if k == 1:
        return NumberToSymbol(num)
    return NumberToPattern2(num//4, k-1) + NumberToSymbol(num % 4)
