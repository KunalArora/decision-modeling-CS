from pulp import *
import numpy as np


class LinearProgram:
    def __init__(self):
        self.prob = LpProblem("Maximize site visit", LpMaximize)
        self.var = [LpVariable(str(i), 0, 1, LpInteger) for i in range(13)]
        self.place_map = {}
        self.duration_map = {}
        self.price_map = {}
        self.distance_map = {}
        self.appreciation_map = {}

    def main_algo(self):
        places = ['TE', 'ML', 'AT', 'MO', 'JT', 'CA', 'CP', 'CN', 'BS', 'SC', 'PC', 'TM', 'AC']
        self.place_map = {str(i): pl for i, pl in enumerate(places)}

        durations = [4.5, 3, 1, 2, 1.5, 2, 2.5, 2, 2, 1.5, 0.75, 2, 1.5]
        self.duration_map = {str(i): pl for i, pl in enumerate(durations)}

        prices = [15.5, 12, 9.5, 11, 0, 10, 10, 5, 8, 8.5, 0, 15, 0]
        self.price_map = {str(i): pl for i, pl in enumerate(prices)}

        duration = 0.
        price = 0.
        for i in range(13):
            duration += durations[i] * self.var[i]
            price += prices[i] * self.var[i]

        self.prob += sum(self.var), "Max # of places visited"

        # Constraints
        self.prob += price <= 65.0, "price constraint"
        self.prob += duration <= 12.0, "distance constraint"


        distance_string = ("0 3.8 2.1 2.4 3.5 4.2 5.0 4.4 5.5 4.2 2.5 3.1 1.9\
            0 3.8 1.1 1.3 3.3 1.3 1.1 3.4 0.800 1.7 2.5 2.8\
            0 3.1 3.0 5.8 4.8 4.9 4.3 4.6 2.2 4.4 1.0\
            0 0.900 3.1 2.5 2.0 3.9 1.8 1.0 2.3 2.1\
            0 4.2 2.0 2.4 2.7 2.0 1.0 3.4 2.1\
            0 3.5 2.7 6.5 2.6 3.8 1.3 4.9\
            0 0.850 3.7 0.900 2.7 3.4 3.8\
            0 4.5 0.400 2.8 2.7 3.9\
            0 4.2 3.3 5.7 3.8\
            0 2.5 2.6 3.6\
            0 3.0 1.2\
            0 2.1\
            0")

        for i in range(13):
            current_distances = distance_string.split("            ")[i].split(" ")
            for j in range(i, 13):
                # print(i,j, current_distances[j-i])
                self.distance_map[(i,j)] = float(current_distances[j-i])

    def pref1_constraint(self):
         for i in range(13):
            for j in range(i+1, 13):
                if self.distance_map[(i,j)]<=1:
                    # print(self.place_map[str(i)], self.place_map[str(j)])
                    self.prob += (self.var[i] - self.var[j] == 0), f"Visits both or only one of {self.place_map[str(i)]}, {self.place_map[str(j)]} within 1km"

    def pref2_constraint(self):
        self.prob += (self.var[5] == 1), "TE visit"
        self.prob += (self.var[0] == 1), "CA visit"

    def pref3_constraint(self):
        self.prob += (self.var[7] + self.var[9] <=1), "Visit CN then not visit SC"

    def pref4_constraint(self):
        self.prob += self.var[11] == 1, "Absolutely visits TM"

    def pref5_constraint(self):
        self.prob += (self.var[1] - self.var[6] <= 0)

    def pref_constraints(self, val):
        if val == 1:
            self.pref1_constraint()
        elif val == 2:
            self.pref2_constraint()
        elif val == 3:
            self.pref3_constraint()
        elif val == 4:
            self.pref4_constraint()
        elif val == 5:
            self.pref5_constraint()
        elif val == 12:
            self.pref1_constraint()
            self.pref2_constraint()
        elif val == 13:
            self.pref1_constraint()
            self.pref3_constraint()
        elif val == 14:
            self.pref1_constraint()
            self.pref4_constraint()
        elif val == 25:
            self.pref2_constraint()
            self.pref5_constraint()
        elif val == 34:
            self.pref3_constraint()
            self.pref4_constraint()
        elif val == 45:
            self.pref4_constraint()
            self.pref5_constraint()
        elif val == 124:
            self.pref1_constraint()
            self.pref2_constraint()
            self.pref4_constraint()
        elif val == 235:
            self.pref2_constraint()
            self.pref3_constraint()
            self.pref5_constraint()
        elif val == 2345:
            self.pref2_constraint()
            self.pref3_constraint()
            self.pref4_constraint()
            self.pref5_constraint()
        elif val == 1245:
            self.pref1_constraint()
            self.pref2_constraint()
            self.pref4_constraint()
            self.pref5_constraint()
        elif val == 12345:
            self.pref1_constraint()
            self.pref2_constraint()
            self.pref3_constraint()
            self.pref4_constraint()
            self.pref5_constraint()

    def weighted_recommendation(self):
        places = ['TE', 'ML', 'AT', 'MO', 'JT', 'CA', 'CP', 'CN', 'BS', 'SC', 'PC', 'TM', 'AC']
        self.place_map = {str(i): pl for i, pl in enumerate(places)}

        durations = np.array([4.5, 3, 1, 2, 1.5, 2, 2.5, 2, 2, 1.5, 0.75, 2, 1.5])
        self.duration_map = {str(i): pl for i, pl in enumerate(durations)}
        durations = (durations-np.min(durations))/np.max(durations)


        prices = np.array([15.5, 12, 9.5, 11, 0, 10, 10, 5, 8, 8.5, 0, 15, 0])
        self.price_map = {str(i): pl for i, pl in enumerate(prices)}
        prices = (prices-np.min(prices))/np.max(prices)

        appreciations = np.array([5,4,3,2,3,4,1,5,4,1,3,2,5])
        self.appreciation_map = {str(i): ap for i, ap in enumerate(appreciations)}
        appreciations = (appreciations-np.min(appreciations))/np.max(appreciations)

        duration = 0.
        price = 0.
        appreciation = 0.
        for i in range(13):
            duration += durations[i] * self.var[i]
            price += prices[i] * self.var[i]
            appreciation += appreciations[i] * self.var[i]

        self.prob += (2*appreciation - 3*price - 4*duration), "Weighted recommendation"

    def print_solution(self, appreciation=False):
        self.prob.solve()

        if appreciation:
            p = 0
            d = 0
            result = []
            print("Seleced places:")
            for i, v in enumerate(self.prob.variables()):
                if v.varValue == 1:
                    print(f"\t{self.place_map[v.name]}, duration={self.duration_map[v.name]}, price={self.price_map[v.name]}, appreciation={self.appreciation_map[v.name]}")
        else:
            p = 0
            d = 0
            result = []
            for i, v in enumerate(self.prob.variables()):
                if v.varValue == 1:
                    p += self.price_map[v.name]
                    d += self.duration_map[v.name]
                    result.append(self.place_map[v.name])

            print("Problem Status: " + LpStatus[self.prob.status])
            print("Resulted places visited: " + str(result))
            print("Total duration spend: " + str(d))
            print("Total price spend: " + str(p))


if __name__ == "__main__":
    print("\nQuestion1:")
    LinearProgQues1 = LinearProgram()
    LinearProgQues1.main_algo()
    LinearProgQues1.print_solution()

    for i in range(0,5):
        print(f"\nQuestion2a - Pref{i+1} :")
        obj = (f"LinearProgQues2a_{i+1}")
        obj = LinearProgram()
        obj.main_algo()
        obj.pref_constraints(i+1)
        obj.print_solution()

    print(f"\nQuestion2b - Pref1 & 2:")
    obj = ("LinearProgQues2b_" + "12" )
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(12)
    obj.print_solution()

    print(f"\nQuestion2c - Pref1 & 3:")
    obj = ("LinearProgQues2c_" + "13" )
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(13)
    obj.print_solution()

    print(f"\nQuestion2d - Pref1 & 4:")
    obj = ("LinearProgQues2d_" + "14" )
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(14)
    obj.print_solution()

    print(f"\nQuestion2e - Pref2 & 5:")
    obj = ("LinearProgQues2e_" + "25" )
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(25)
    obj.print_solution()

    print(f"\nQuestion2f - Pref3 & 4:")
    obj = ("LinearProgQues2f_" + "34" )
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(34)
    obj.print_solution()

    print(f"\nQuestion2g - Pref4 & 5:")
    obj = ("LinearProgQues2g_" + "45")
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(45)
    obj.print_solution()

    print(f"\nQuestion2h - Pref1 & 2 & 4:")
    obj = ("LinearProgQues2h_" + "124")
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(124)
    obj.print_solution()

    print(f"\nQuestion2i - Pref2 & 3 & 5:")
    obj = ("LinearProgQues2i_" + "235")
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(235)
    obj.print_solution()

    print(f"\nQuestion2j - Pref2 & 3 & 4 & 5:")
    obj = ("LinearProgQues2j_" + "2345")
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(2345)
    obj.print_solution()

    print(f"\nQuestion2k - Pref1 & 2 & 4 & 5:")
    obj = ("LinearProgQues2k_" + "1245")
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(1245)
    obj.print_solution()

    print(f"\nQuestion2l - Pref1 & 2 & 3 & 4 & 5:")
    obj = ("LinearProgQues2l_" + "12345")
    obj = LinearProgram()
    obj.main_algo()
    obj.pref_constraints(12345)
    obj.print_solution()

    print(f"\nQuestion4:")
    # obj = ("LinearProgQues2l_" + "12345")
    obj = LinearProgram()
    obj.weighted_recommendation()
    obj.print_solution(appreciation=True)

"""

1. ListVisit1: 'PC', 'AC', 'AT', 'MO', 'CN', 'BS', 'SC'

2   (a1) ['PC', 'TM', 'AC', 'AT', 'MO', 'JT', 'CA']
    (a2) ['TE', 'PC', 'AC', 'AT', 'CA', 'SC']
    (a3) ['PC', 'AC', 'AT', 'MO', 'CA', 'BS', 'SC']
    (a4) ['PC', 'TM', 'AC', 'AT', 'CA', 'BS', 'SC']
    (a5) ['PC', 'AC', 'AT', 'MO', 'CN', 'BS', 'SC']

    (b). ['TE', 'AC', 'AT', 'CA', 'BS']
    (c). ['PC', 'TM', 'AC', 'AT', 'MO', 'JT', 'CA']
    (d). ['PC', 'TM', 'AC', 'AT', 'MO', 'JT', 'CA']
    (e). ['TE', 'PC', 'AC', 'AT', 'CA', 'SC']
    (f). ['PC', 'TM', 'AC', 'AT', 'CA', 'BS', 'SC']
    (g). ['PC', 'TM', 'AC', 'AT', 'CA', 'BS', 'SC']
    (h). ['TE', 'TM', 'AC', 'AT', 'CA']
    (i). ['TE', 'PC', 'AC', 'AT', 'JT', 'CA']
    (j). ['TE', 'PC', 'TM', 'AC', 'AT', 'CA']
    (k). ['TE', 'TM', 'AC', 'AT', 'CA']
    (l). ['TE', 'TM', 'AC', 'AT', 'CA']
    (m). Yes, the solution in ListVisit 1 is close to varous recommendations in Question 2. 
        This is because we are restricting the search space in Question 2 by adding additional constraints. 
        However, the optimal solution favours the presence of low duration places 
        (we note that the duration constraint is exceeded in all cases before the preice constarint) in the itinerary.

3.
    The preference ranking is:
        TN ~ CN ~ AC > ML ~ CA ~ BS > AT ~ JT ~ PC > MO ~ TM > CP ~ SC
    The preference for places in ListVisit1 is:
        CN ~ AC > BS > AT ~ PC > MO > SC
    The recommendations in Question 2 seem to be independent of the appreciation preference(inferred from the apppreciation scores).

4.
    We first assign appreciation score to each place as 1,2,3,4 or 5 based on the number of star ratings.
    This scoring preserves the Qualitative preference information provided by the ratings.
    Next, we normalize the appreciation score such that the max score is 1.0 and the min score is 0.0.
    Then, we calculate the total appreciation (normalised) of places in the itinerary (say appreciation).
    Similarly, we normalise and compute the corresponding values for price and duration (as price and duration).
    Now, the Objective function to maximise is calculated as:
        2*appreciation - 3*price - 4*duration

    The normalisation step is important to ensure that the values of appreciation, price and duration are comparable to each other.
    The recommendation provided is as follows:
        PC, duration=0.75, price=0.0, appreciation=3
        AC, duration=1.5, price=0.0, appreciation=5
        JT, duration=1.5, price=0.0, appreciation=3
"""