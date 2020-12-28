# If you really get math into your heart, it's like a poem or a beautiful song.

# heart + math = rhyme

for ia in range(1, 10):
    for ib in range(0, 10):
        for ic in range(0, 10):
            for id in range(1, 10):
                for ie in range(0, 10):
                    for ig in range(1, 10):
                        for ih in range(0, 10):
                            h = str(ia)
                            e = str(ib)
                            a = str(ic)
                            r = str(id)
                            t = str(ie)
                            m = str(ig)
                            y = str(ih)

                            first_word = int(h + e + a + r + t)
                            second_word = int(m + a + t + h)
                            answer = int(r + h + y + m + e)

                            letters = [h, e, a, r, t, m, y]
                            if (first_word + second_word == answer) and (len(set(letters)) == len(letters)):
                                print(first_word, second_word, answer)
                                print("heart math rhyme")
                                print()

# 19 s

# 46952 7924 54876
# heart math rhyme