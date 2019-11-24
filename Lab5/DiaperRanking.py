from pulp import *
from copy import deepcopy


def CheckAdditiveModel_1():
    prob = LpProblem("PL1", LpMaximize)

    eps = LpVariable("Eps", 0, None)

    u_1a = LpVariable("U_1a", 17, 20)
    u_2a = LpVariable("U_2a", 17, 20)
    u_2c = LpVariable("U_2c", 17, 20)
    u_2d = LpVariable("U_2d", 17, 20)

    u_1b = LpVariable("U_1b", 13, 16.5)
    u_2b = LpVariable("U_2b", 13, 16.5)
    u_1f = LpVariable("U_1f", 13, 16.5)
    u_1g = LpVariable("U_1g", 13, 16.5)
    u_1i = LpVariable("U_1i", 13, 16.5)
    u_1j = LpVariable("U_1j", 13, 16.5)
    u_1k = LpVariable("U_1k", 13, 16.5)

    u_1c = LpVariable("U_1c", 10, 12.5)
    u_1d = LpVariable("U_1d", 10, 12.5)
    u_1e = LpVariable("U_1e", 10, 12.5)
    u_2e = LpVariable("U_2e", 10, 12.5)
    u_1f = LpVariable("U_1f", 10, 12.5)
    u_2f = LpVariable("U_2f", 10, 12.5)
    u_1h = LpVariable("U_1h", 10, 12.5)
    u_1l = LpVariable("U_1l", 10, 12.5)

    u_2g = LpVariable("U_2g", 7, 9.5)
    u_2h = LpVariable("U_2h", 7, 9.5)
    u_2i = LpVariable("U_2i", 7, 9.5)

    u_2j = LpVariable("U_2j", 0, 6.5)
    u_2k = LpVariable("U_2k", 0, 6.5)
    u_2l = LpVariable("U_2l", 0, 6.5)

    fa = 0.6 * u_1a + 0.4 * u_2a
    fb = 0.6 * u_1b + 0.4 * u_2b
    fc = 0.6 * u_1c + 0.4 * u_2c
    fd = 0.6 * u_1d + 0.4 * u_2d
    fe = 0.6 * u_1e + 0.4 * u_2e
    ff = 0.6 * u_1f + 0.4 * u_2f
    fg = 0.6 * u_1g + 0.4 * u_2g
    fh = 0.6 * u_1h + 0.4 * u_2h
    fi = 0.6 * u_1i + 0.4 * u_2i
    fj = 0.6 * u_1j + 0.4 * u_2j
    fk = 0.6 * u_1k + 0.4 * u_2k
    fl = 0.6 * u_1l + 0.4 * u_2l

    prob += eps
    prob += fa >= fb + eps
    prob += fb >= fc + eps
    prob += fc == fd
    prob += fd == fe
    prob += fe == ff
    prob += ff >= fg + eps
    prob += fg == fh
    prob += fh >= fi + eps
    prob += fi == fj
    prob += fj == fk
    prob += fk >= fl + eps

    prob += fa == 17
    prob += fb == 14.5
    prob += fc == 12.5
    prob += fd == 12.5
    prob += fe == 12.5
    prob += ff == 12.5
    prob += fg == 12
    prob += fh == 12
    prob += fi == 9.5
    prob += fj == 9.5
    prob += fk == 9.5
    prob += fl == 6.5

    prob.writeLP("CheckAdditiveModel_1.lp")

    return prob.status > 0


def CheckAdditiveModel_2():
    prob = LpProblem("PL1", LpMaximize)

    eps = LpVariable("Eps", 0, None)

    u_1a = LpVariable("U_1a", 17, 20)
    u_2a = LpVariable("U_2a", 17, 20)
    u_2c = LpVariable("U_2c", 17, 20)
    u_2d = LpVariable("U_2d", 17, 20)

    u_1b = LpVariable("U_1b", 13, 16.5)
    u_2b = LpVariable("U_2b", 13, 16.5)
    u_1f = LpVariable("U_1f", 13, 16.5)
    u_1g = LpVariable("U_1g", 13, 16.5)
    u_1i = LpVariable("U_1i", 13, 16.5)
    u_1j = LpVariable("U_1j", 13, 16.5)
    u_1k = LpVariable("U_1k", 13, 16.5)

    u_1c = LpVariable("U_1c", 10, 12.5)
    u_1d = LpVariable("U_1d", 10, 12.5)
    u_1e = LpVariable("U_1e", 10, 12.5)
    u_2e = LpVariable("U_2e", 10, 12.5)
    u_1f = LpVariable("U_1f", 10, 12.5)
    u_2f = LpVariable("U_2f", 10, 12.5)
    u_1h = LpVariable("U_1h", 10, 12.5)
    u_1l = LpVariable("U_1l", 10, 12.5)

    u_2g = LpVariable("U_2g", 7, 9.5)
    u_2h = LpVariable("U_2h", 7, 9.5)
    u_2i = LpVariable("U_2i", 7, 9.5)

    u_2j = LpVariable("U_2j", 0, 6.5)
    u_2k = LpVariable("U_2k", 0, 6.5)
    u_2l = LpVariable("U_2l", 0, 6.5)

    fa = 0.6 * u_1a + 0.4 * u_2a
    fb = 0.6 * u_1b + 0.4 * u_2b
    fc = 0.6 * u_1c + 0.4 * u_2c
    fd = 0.6 * u_1d + 0.4 * u_2d
    fe = 0.6 * u_1e + 0.4 * u_2e
    ff = 0.6 * u_1f + 0.4 * u_2f
    fg = 0.6 * u_1g + 0.4 * u_2g
    fh = 0.6 * u_1h + 0.4 * u_2h
    fi = 0.6 * u_1i + 0.4 * u_2i
    fj = 0.6 * u_1j + 0.4 * u_2j
    fk = 0.6 * u_1k + 0.4 * u_2k
    fl = 0.6 * u_1l + 0.4 * u_2l

    prob += eps
    prob += fa >= fb + eps
    prob += fb >= fc + eps
    prob += fc == fd
    prob += fd == fe
    prob += fe == ff
    prob += ff >= fg + eps
    prob += fg == fh
    prob += fh >= fi + eps
    prob += fi == fj
    prob += fj == fk
    prob += fk >= fl + eps

    prob.writeLP("CheckAdditiveModel_2.lp")

    prob.solve()
    print(fa.name)

    return prob.status > 0


def CheckAdditiveModel_3():
    eps = LpVariable("Eps", 0, None)

    u_1a = LpVariable("U_1a", 17, 20)
    u_2a = LpVariable("U_2a", 17, 20)
    u_2c = LpVariable("U_2c", None, 20)
    u_2d = LpVariable("U_2d", 17, 20)

    u_1b = LpVariable("U_1b", 13, 16.5)
    u_2b = LpVariable("U_2b", 13, 16.5)
    u_1f = LpVariable("U_1f", 13, 16.5)
    u_1g = LpVariable("U_1g", 13, 16.5)
    u_1i = LpVariable("U_1i", 13, 16.5)
    u_1j = LpVariable("U_1j", 13, 16.5)
    u_1k = LpVariable("U_1k", 13, 16.5)

    u_1c = LpVariable("U_1c", 10, 12.5)
    u_1d = LpVariable("U_1d", 10, 12.5)
    u_1e = LpVariable("U_1e", 10, 12.5)
    u_2e = LpVariable("U_2e", 10, 12.5)
    u_1f = LpVariable("U_1f", 10, 12.5)
    u_2f = LpVariable("U_2f", 10, 12.5)
    u_1h = LpVariable("U_1h", 10, 12.5)
    u_1l = LpVariable("U_1l", 10, 12.5)

    u_2g = LpVariable("U_2g", 7, 9.5)
    u_2h = LpVariable("U_2h", 7, 9.5)
    u_2i = LpVariable("U_2i", 7, 9.5)

    u_2j = LpVariable("U_2j", 0, 6.5)
    u_2k = LpVariable("U_2k", 0, 6.5)
    u_2l = LpVariable("U_2l", 0, 6.5)

    fa = 0.6 * u_1a + 0.4 * u_2a
    fb = 0.6 * u_1b + 0.4 * u_2b
    fc = 0.6 * u_1c + 0.4 * u_2c
    fd = 0.6 * u_1d + 0.4 * u_2d
    fe = 0.6 * u_1e + 0.4 * u_2e
    ff = 0.6 * u_1f + 0.4 * u_2f
    fg = 0.6 * u_1g + 0.4 * u_2g
    fh = 0.6 * u_1h + 0.4 * u_2h
    fi = 0.6 * u_1i + 0.4 * u_2i
    fj = 0.6 * u_1j + 0.4 * u_2j
    fk = 0.6 * u_1k + 0.4 * u_2k
    fl = 0.6 * u_1l + 0.4 * u_2l

    for i, f in enumerate([fa, fl]):
        for j, factor in enumerate([LpMaximize, LpMinimize]):
            prob = LpProblem("PL1", factor)
            prob += f
            prob += fa >= fb + eps
            prob += fb >= fc + eps
            prob += fc == fd
            prob += fe == ff
            prob += ff >= fg + eps
            prob += fg == fh
            prob += fh >= fi + eps
            prob += fj == fk
            prob += fk >= fl + eps

            print("{} {}".format("Maximizing" if j == 0 else "Minimizing", "fa" if i == 0 else "fl"))
            prob.writeLP("CheckAdditiveModel_3_{}_{}.lp".format(i, j))
            prob.solve()
            print(
                "The ranking produced by the magazine with the given global score is {}compatible with a weighted sum model.".format(
                    "" if prob.status > 0 else "not "))
            print("fa = {}.{}".format(fa.value(), " Better than magazine score." if fa.value() > 17 else ""))
            print("fb = {}.{}".format(fb.value(), " Better than magazine score." if fb.value() > 14.5 else ""))
            print("fc = {}.{}".format(fc.value(), " Better than magazine score." if fc.value() > 12.5 else ""))
            print("fd = {}.{}".format(fd.value(), " Better than magazine score." if fd.value() > 12.5 else ""))
            print("fe = {}.{}".format(fe.value(), " Better than magazine score." if fe.value() > 12.5 else ""))
            print("ff = {}.{}".format(ff.value(), " Better than magazine score." if ff.value() > 12.5 else ""))
            print("fg = {}.{}".format(fg.value(), " Better than magazine score." if fg.value() > 12 else ""))
            print("fh = {}.{}".format(fh.value(), " Better than magazine score." if fh.value() > 12 else ""))
            print("fi = {}.{}".format(fi.value(), " Better than magazine score." if fi.value() > 9.5 else ""))
            print("fj = {}.{}".format(fj.value(), " Better than magazine score." if fj.value() > 9.5 else ""))
            print("fk = {}.{}".format(fk.value(), " Better than magazine score." if fk.value() > 9.5 else ""))
            print("fl = {}.{}".format(fl.value(), " Better than magazine score." if fl.value() > 6.5 else ""))


def CompareRankings(results):
    concordant, discordant = CompareRankingsHelper(results)

    return (concordant - discordant) / (concordant + discordant)


def CompareRankingsHelper(results):
    if len(results) == 1:
        return 0.0, 0.0

    results_copy = deepcopy(results)
    results_copy.pop(0)
    concordant, discordant = CompareRankingsHelper(results_copy)
    for i in range(1, len(results)):
        if results[i] >= results[0]:
            concordant += 1
        else:
            discordant += 1
    return concordant, discordant


def CheckAdditiveModel_4():
    eps = LpVariable("Eps", 0, None)

    u_1a = LpVariable("U_1a", 17, 20)
    u_2a = LpVariable("U_2a", 17, 20)
    u_2c = LpVariable("U_2c", None, 20)
    u_2d = LpVariable("U_2d", 17, 20)

    u_1b = LpVariable("U_1b", 13, 16.5)
    u_2b = LpVariable("U_2b", 13, 16.5)
    u_1f = LpVariable("U_1f", 13, 16.5)
    u_1g = LpVariable("U_1g", 13, 16.5)
    u_1i = LpVariable("U_1i", 13, 16.5)
    u_1j = LpVariable("U_1j", 13, 16.5)
    u_1k = LpVariable("U_1k", 13, 16.5)

    u_1c = LpVariable("U_1c", 10, 12.5)
    u_1d = LpVariable("U_1d", 10, 12.5)
    u_1e = LpVariable("U_1e", 10, 12.5)
    u_2e = LpVariable("U_2e", 10, 12.5)
    u_1f = LpVariable("U_1f", 10, 12.5)
    u_2f = LpVariable("U_2f", 10, 12.5)
    u_1h = LpVariable("U_1h", 10, 12.5)
    u_1l = LpVariable("U_1l", 10, 12.5)

    u_2g = LpVariable("U_2g", 7, 9.5)
    u_2h = LpVariable("U_2h", 7, 9.5)
    u_2i = LpVariable("U_2i", 7, 9.5)

    u_2j = LpVariable("U_2j", 0, 6.5)
    u_2k = LpVariable("U_2k", 0, 6.5)
    u_2l = LpVariable("U_2l", 0, 6.5)

    fa = LpAffineExpression(0.6 * u_1a + 0.4 * u_2a, name="fa")
    fb = LpAffineExpression(0.6 * u_1b + 0.4 * u_2b, name="fb")
    fc = LpAffineExpression(0.6 * u_1c + 0.4 * u_2c, name="fc")
    fd = LpAffineExpression(0.6 * u_1d + 0.4 * u_2d, name="fd")
    fe = LpAffineExpression(0.6 * u_1e + 0.4 * u_2e, name="fe")
    ff = LpAffineExpression(0.6 * u_1f + 0.4 * u_2f, name="ff")
    fg = LpAffineExpression(0.6 * u_1g + 0.4 * u_2g, name="fg")
    fh = LpAffineExpression(0.6 * u_1h + 0.4 * u_2h, name="fh")
    fi = LpAffineExpression(0.6 * u_1i + 0.4 * u_2i, name="fi")
    fj = LpAffineExpression(0.6 * u_1j + 0.4 * u_2j, name="fj")
    fk = LpAffineExpression(0.6 * u_1k + 0.4 * u_2k, name="fk")
    fl = LpAffineExpression(0.6 * u_1l + 0.4 * u_2l, name="fl")

    min_ranking = []
    max_ranking = []
    for i, f in enumerate([fa, fb, fc, fd, fe, ff, fg, fh, fi, fj, fk, fl]):
        f_str = f.name
        score = []

        for j, factor in enumerate([LpMinimize, LpMaximize]):
            prob = LpProblem("PL1", factor)
            prob += f

            prob.writeLP("CheckAdditiveModel_4_{}_{}.lp".format(i, j))
            prob.solve()
            score.append(f.value())

        print("{}: {}".format(f_str, score))
        min_ranking.insert(0, score[0])
        max_ranking.insert(1, score[1])

    print("Tau coefficient between magazine ranking and ranking of maximization:", CompareRankings(max_ranking))
    print("Tau coefficient between magazine ranking and ranking of minimization:", CompareRankings(min_ranking))


if __name__ == "__main__":
    print("\nQuestion 1")
    print(
        "The ranking produced by the magazine with the given global score is {} compatible with a weighted sum "
        "model.".format("" if CheckAdditiveModel_1() else "not"))
    print("\nQuestion 2.1")
    print(
        "The ranking produced by the magazine with the given global score is {} compatible with a weighted sum "
        "model.".format("" if CheckAdditiveModel_2() else "not"))

    print("\nQuestion 2.2")
    CheckAdditiveModel_3()

    print("\nQuestion 3")
    CheckAdditiveModel_4()
