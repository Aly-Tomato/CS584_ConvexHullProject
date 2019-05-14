import Utils
import Jarvis
import Grahams
import time

ROUND = 4 #round to ith of second
RANGE = 1000 #total number of tests to run
INIT_SIZE = 30 #initial size of list

def print_test_name(test,distr):
    print("*******************************")
    print(f" Performing:\t{test} ")
    print(f" Distribution:\t{distr} ")
    print("*******************************")

def do_test(test,data_set):
    if test == "Jarvis Algorithm":
        t1 = time.perf_counter()
        Jarvis.do_Jarvis(data_set)
        t = time.perf_counter()
    else:
        t1 = time.perf_counter()
        Grahams.do_Grahams(data_set)
        t = time.perf_counter()
    return t-t1

def main():
    tests = ["Jarvis Algorithm","Graham Scan"]
    test_type = "Random"
    for test_name in tests:
     print_test_name(test_name, test_type)
     size = INIT_SIZE
     for i in range(0,RANGE):
         ticks = do_test(test_name, Utils.make_random_list(size))
         Utils.write_test_results([test_name+test_type, size,round(ticks,ROUND)])
         size += 10
     print(f"{test_name} complete!\n")

    test_type = "Min Hull Points"
    for test_name in tests:
        print_test_name(test_name, test_type)
        size = INIT_SIZE
        for i in range(0,RANGE):
            ticks = do_test(test_name+test_type, Utils.make_minhull_list(size))
            Utils.write_test_results([test_name, size,round(ticks,ROUND)])
            size += 10
        print(f"{test_name} complete!\n")

    test_type = "All Hull Points"
    for test_name in tests:
        print_test_name(test_name, test_type)
        size = INIT_SIZE
        for i in range(0,RANGE-500):
            ticks = do_test(test_name, Utils.make_maxhull_list(size))
            Utils.write_test_results([test_name+test_type, size,round(ticks,ROUND)])
            size += 10
        print(f"{test_name} complete!\n")

if __name__ == "__main__":
    main()
