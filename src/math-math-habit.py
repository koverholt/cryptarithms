# Sometimes, to get good at math, you just need to practice and practice until
# it becomes a habit.

# math + math = habit

for ia in range(1, 10):
    for ib in range(0, 10):
        for ic in range(0, 10):
            for id in range(1, 10):
                for ie in range(0, 10):
                    for ig in range(0, 10):
                        m = str(ia)
                        a = str(ib)
                        t = str(ic)
                        h = str(id)
                        b = str(ie)
                        i = str(ig)

                        first_word = int(m + a + t + h)
                        second_word = int(m + a + t + h)
                        answer = int(h + a + b + i + t)

                        letters = [m, a, t, h, b, i]
                        if (first_word + second_word == answer) and (len(set(letters)) == len(letters)):
                            print(first_word, second_word, answer)
                            print("math math habit")
                            print()

# 2 s

# 7521 7521 15042
# math math habit