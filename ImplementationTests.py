import Utils
import Jarvis
import Grahams

def test_minhull(algo):
    """
    Tests that check_minhull_list method correctly returns a list
    with exactly 3 points on the hull
    """
    size = 100
    err_count = 0
    if(algo == "Jarvis"):
        for i in range(0, 100):
            if len(Jarvis.do_Jarvis(Utils.make_minhull_list(size))) != 3:
                err_count += 1
            size += 10
        return err_count
    else:
        for i in range(0, 100):
            if len(Grahams.do_Grahams(Utils.make_minhull_list(size))) != 3:
                err_count += 1
            size += 10
        return err_count

def test_maxhull(algo):
    """
    Tests that check_maxhull_list method correctly returns a list
    with all points on the hull
    """
    err_count = 0
    if(algo == "Jarvis"):
        for i in range(3, 60):
            if len(Jarvis.do_Jarvis(Utils.make_maxhull_list(i))) != i:
                err_count += 1
        return err_count
    else:
        for i in range(3, 60):
            if len(Grahams.do_Grahams(Utils.make_maxhull_list(i))) != i:
                err_count += 1
        return err_count


def main():
    algos = ["Jarvis", "Graham"]
    for algo in algos:
        err_count = test_minhull(algo)
        if err_count > 0:
            print("ERROR: min hull list is returning incorrect set")
            print("EXPECTED: 3 points on hull")
            print(f"RESPONDED: {err_count} lists with incorrect total of points on hull using {algo}")
        else:
            print(f"SUCCESS: Min Hull List resulted in correct # of hull points using {algo}")

        err_count = test_maxhull(algo)
        if err_count > 0:
            print("ERROR: max hull list is returning incorrect set")
            print("EXPECTED: all points on hull")
            print(f"RESPONDED: {err_count} lists with incorrect total of points on hull using {algo}")
        else:
            print(f"SUCCESS: Max Hull List resulted in correct # of hull points using {algo}")

if __name__ == "__main__":
    main()