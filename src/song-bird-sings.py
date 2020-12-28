# The song bird sings!
# This puzzle has two solutions.

# song + bird = sings

for ia in range(1, 10):
    for ib in range(0, 10):
        for ic in range(0, 10):
            for id in range(0, 10):
                for ie in range(1, 10):
                    for ig in range(0, 10):
                        for ih in range(0, 10):
                            for ii in range(0, 10):
                                s = str(ia)
                                o = str(ib)
                                n = str(ic)
                                g = str(id)
                                b = str(ie)
                                i = str(ig)
                                r = str(ih)
                                d = str(ii)

                                first_word = int(s + o + n + g)
                                second_word = int(b + i + r + d)
                                answer = int(s + i + n + g + s)

                                letters = [s, o, n, g, b, i, r, d]
                                if (first_word + second_word == answer) and (len(set(letters)) == len(letters)):
                                    print(first_word, second_word, answer)
                                    print("song bird sings")
                                    print()

# 3 min 30 s

# 1453 9078 10531
# song bird sings

# 1673 9058 10731
# song bird sings