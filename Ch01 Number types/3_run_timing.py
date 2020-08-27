def run_timing():
    number_of_runs = 0
    total_of_time = 0
    time = 0
    while ans := input("Enter 10kms run time: "):

        try:
            time = float(ans)
        except ValueError as e:
            print("Please! only numbers!")
        
        if not time:
            break
        total_of_time += time
        number_of_runs += 1

    average = total_of_time / number_of_runs
    print(f"Average of {average: .2f} over {number_of_runs} runs")

def main():
    run_timing()

main()