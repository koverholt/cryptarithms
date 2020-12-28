# This one tells you that if you keep a positive attitude to math, you'll find
# it a treat!

# eager + math = treat

for ia in range(1, 10):
    for ib in range(0, 10):
        for ic in range(0, 10):
            for id in range(0, 10):
                for ie in range(1, 10):
                    for ig in range(1, 10):
                        for ih in range(1, 10):
                            e = str(ia)
                            a = str(ib)
                            g = str(ic)
                            r = str(id)
                            m = str(ie)
                            t = str(ig)
                            h = str(ih)

                            first_word = int(e + a + g + e + r)
                            second_word = int(m + a + t + h)
                            answer = int(t + r + e + a + t)

                            letters = [e, a, g, r, m, t, h]
                            if (first_word + second_word == answer) and (len(set(letters)) == len(letters)):
                                print(first_word, second_word, answer)
                                print("eager math treat")
                                print()

# 18 s

# 14713 8429 23142
# eager math treat