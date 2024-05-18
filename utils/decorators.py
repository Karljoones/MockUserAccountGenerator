import config
import time

# Decorator to output the timing of a function, will output if config.verbose_debugging is set to True
def time_measurement_decorator(func):
    def wrapper_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        if config.verbose_debugging: 
            print(f"[{func.__name__}] Completed in {(end - start):0.4f} seconds.")
    return wrapper_function