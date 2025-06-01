from timeit import default_timer

def stopwatch_with_input():
    input("Press Enter to START the timer...")
    start = default_timer()

    input("Press Enter to STOP the timer...")
    end = default_timer()

    elapsed = end - start
    print(f"Elapsed time: {elapsed:.4f} seconds")

stopwatch_with_input()



