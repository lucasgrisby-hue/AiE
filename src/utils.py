# -*- coding: utf-8 -*-
from datetime import datetime

def process_response(response, stream=False):
    if not stream:
        print(f"AI:\n\n{response}")
    else:
        print("AI:\n\n")
        for chunk in response:
            print(chunk.message.content, end="", flush=True)
        
        print()


def log(func):
    def new_func(*args, **kwargs):
        print(f"[{datetime.now()}] Running {func.__class__.__name__} now!\n\n")
        result = func(*args, **kwargs)
        print(f"\n\n[{datetime.now()}] Done running {func.__class__.__name__} now!")
        return result
    
    return new_func


    