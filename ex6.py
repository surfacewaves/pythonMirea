def main(input_list):
    decision_tree = {"RDOC": {"1998": {"SMT": 0,
                                       "CUDA": 1,
                                       "LASSO": 2},
                              "2010": 3},
                     "MQL4": {"1998": {"SMT": 4,
                                       "CUDA": 5,
                                       "LASSO": 6},
                              "2010": {"SMT": 7,
                                       "CUDA": 8,
                                       "LASSO": 9}
                              }
                     }

    while not isinstance(decision_tree, int):
        for item in input_list:
            if str(item) in decision_tree.keys():
                decision_tree = decision_tree[str(item)]
                break

    return decision_tree


if __name__ == '__main__':
    print(main(['LASSO', 1958, 'MQL4', 2010]))
    print(main(['CUDA', 1986, 'RDOC', 1998]))

# https://www.cyberforum.ru/python-tasks/thread2976373.html
