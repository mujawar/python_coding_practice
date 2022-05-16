def long_words(n,wordstr):
    word_len = []
    txt = wordstr.split(' ')
    print(txt)
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len





print(long_words(3, "The quick brown fox jumps over the lazy dog"))