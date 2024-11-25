import multiprocessing

# Define the worker function
def worker_function(process_number):
    print(f"Hello from process {process_number}!")

# Wrap the multiprocessing logic in a function
def main():
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes have completed.")

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)
    main()