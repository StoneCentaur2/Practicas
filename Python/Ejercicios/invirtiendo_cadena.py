def inves(txt: str):
    num_txt = len(txt)
    final_txt = ''
    for i in range(0, num_txt):
        final_txt += txt[num_txt - i - 1]
    print(final_txt)

inves('odnum aloH')