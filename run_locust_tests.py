import subprocess
import time

def run_locust_tests(file_prefix, locustfile, host):
    start_time = time.time()
    print(f"Starting test: {file_prefix} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    
    command = [
        "locust",
        "-f", locustfile,
        "--headless",
        "-u", "100",  # Number of users
        "-r", "10",   # Spawn rate (users per second)
        "--run-time", "1m",  # Test duration
        "--csv", file_prefix,  # Output file prefix
        "--host", host  # Host URL
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Finished test: {file_prefix} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Results for {file_prefix}:")
    # print(result.stdout)
    # print(result.stderr)

if __name__ == "__main__":
    host = "http://127.0.0.1:8000/"  # ここでホストURLを設定します

    print("Running tests without load balancer...")
    run_locust_tests("locust_results_no_balancer", "locustfile_no_balancer.py", host)

    print("Running tests with load balancer...")
    run_locust_tests("locust_results_balancer", "locustfile_balancer.py", host)