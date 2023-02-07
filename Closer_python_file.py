import time
import sys
import subprocess
import tkinter as tk


def close_after_time(program_name, timeout_minutes):
    timeout_seconds = timeout_minutes * 60
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        try:
            process = subprocess.check_output(["tasklist"])
            if program_name.encode() in process:
                time.sleep(1)
            else:
                break
        except subprocess.CalledProcessError as e:
            print(e)
            sys.exit()
    subprocess.run(["taskkill", "/IM", program_name], shell=True)


def on_submit():
    program_name = entry_program_name.get()
    timeout_minutes = int(entry_timeout.get())
    close_after_time(program_name, timeout_minutes)
    label_result.config(text="Program closed after specified time.")


root = tk.Tk()
root.geometry("300x150")
root.title("End Timer")

label_program_name = tk.Label(root, text="Enter program name:")
label_program_name.pack()

entry_program_name = tk.Entry(root)
entry_program_name.pack()

label_timeout = tk.Label(root, text="Enter timeout in minutes:")
label_timeout.pack()

entry_timeout = tk.Entry(root)
entry_timeout.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
