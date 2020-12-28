# When you become mighty at math, you'll find it a lot less stressful!

# might + math = happy

for ia in range(1, 10):
    for ib in range(0, 10):
        for ic in range(0, 10):
            for id in range(1, 10):
                for ie in range(0, 10):
                    for ig in range(0, 10):
                        for ih in range(0, 10):
                            for ii in range(0, 10):
                                m = str(ia)
                                i = str(ib)
                                g = str(ic)
                                h = str(id)
                                t = str(ie)
                                a = str(ig)
                                p = str(ih)
                                y = str(ii)

                                first_word = int(m + i + g + h + t)
                                second_word = int(m + a + t + h)
                                answer = int(h + a + p + p + y)

                                letters = [m, i, g, h, t, a, p, y]
                                if (first_word + second_word == answer) and (len(set(letters)) == len(letters)):
                                    print(first_word, second_word, answer)
                                    print("might math happy")
                                    print()

# 3 min 54 s

# 65873 6237 72110
# might math happy