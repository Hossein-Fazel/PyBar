# Progress Bar in Python

This is a simple Python program that implements a customizable cli progress bar. The progress bar can be used to visually represent the progress of a task, such as file downloads, data processing, or any other operation that can be broken down into incremental steps.

## Features

- **Customizable Characters**: You can specify the characters used to represent filled and empty portions of the progress bar.
- **Adjustable Size**: The length of the progress bar can be adjusted to fit your needs.
- **Dynamic Updates**: The progress bar updates dynamically as the task progresses.
- **Start and Stop Control**: You can start, update, and stop the progress bar as needed.

### Class Initialization

The `progressbar` class can be initialized with the following parameters:

- `filled` (str): The character used to represent the filled portion of the progress bar. Default is `"#"`.
- `empty_char` (str): The character used to represent the empty portion of the progress bar. Default is `" "` (space).
- `total` (int): The total number of steps required to complete the task. Default is `100`.
- `size` (int): The length of the progress bar in characters. Default is `50`.
- `start` (int): The starting point of the progress bar. Default is `0`.

### Methods

- `reset()`: Resets the progress bar to its initial state.
- `update(value: int)`: Updates the progress bar by the specified value.
- `show()`: Displays the current state of the progress bar.
- `stop()`: Stops the progress bar and prints a new line.

## Usage

### Installation

No installation is required. Simply copy the `progressbar` class into your Python script.


### Example Usage

Here is some examples of how to use the progressbar class:

### Example 1: Custom Filled and Empty Characters
You can use different characters for the filled and empty portions of the progress bar.

```python
from time import sleep

# Create a progress bar with "=" as the filled character and "." as the empty character
tpb = progressbar(filled="=", empty_char=".", total=100, size=50)

# Simulate a task that takes 100 steps
for i in range(100):
    tpb.update(1)
    tpb.show()
    sleep(0.05)  # Simulate a shorter delay

tpb.stop()
```

**Output:**
```plaintext
[=========================.........................] 50.0%
[==================================================] 100.0%
```

---

### Example 2: Smaller Progress Bar
You can create a smaller progress bar for compact displays.

```python
from time import sleep

# Create a smaller progress bar with a size of 20
tpb = progressbar(filled="#", empty_char=" ", total=100, size=20)

# Simulate a task that takes 100 steps
for i in range(100):
    tpb.update(1)
    tpb.show()
    sleep(0.1)

tpb.stop()
```

**Output:**
```plaintext
[##########          ] 50.0%
[####################] 100.0%
```

---

### Example 3: Progress Bar with a Starting Value
You can initialize the progress bar with a starting value other than `0`.

```python
from time import sleep

# Create a progress bar starting at 30 out of 100
tpb = progressbar(filled="#", empty_char=" ", total=100, size=50, start=30)

# Simulate a task that takes 70 steps (to reach 100)
for i in range(70):
    tpb.update(1)
    tpb.show()
    sleep(0.1)

tpb.stop()
```

**Output:**
```plaintext
[###############                             ] 30.0%
[############################################] 100.0%
```

---

### Example 4: Progress Bar for a Smaller Total
You can use the progress bar for tasks with a smaller total number of steps.

```python
from time import sleep

# Create a progress bar for a task with only 10 steps
tpb = progressbar(filled="#", empty_char=" ", total=10, size=20)

# Simulate a task that takes 10 steps
for i in range(10):
    tpb.update(1)
    tpb.show()
    sleep(0.5)  # Simulate a longer delay

tpb.stop()
```

**Output:**
```plaintext
[##########          ] 50.0%
[####################] 100.0%
```

---

### Example 5: Progress Bar with Unicode Characters
You can use Unicode characters for a more visually appealing progress bar.

```python
from time import sleep

# Create a progress bar with a block character (█) as the filled character
tpb = progressbar(filled="█", empty_char="░", total=100, size=40)

# Simulate a task that takes 100 steps
for i in range(100):
    tpb.update(1)
    tpb.show()
    sleep(0.05)

tpb.stop()
```

**Output:**
```plaintext
[████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 50.0%
[████████████████████████████████████████████] 100.0%
```

---

### Example 6: Progress Bar for File Download Simulation
You can use the progress bar to simulate a file download.

```python
from time import sleep

# Simulate downloading a 10 MB file in 1 MB chunks
file_size_mb = 10
chunk_size_mb = 1

# Create a progress bar with a total of 10 steps (1 step per MB)
tpb = progressbar(filled="#", empty_char=" ", total=file_size_mb, size=30)

print("Downloading file...")
for i in range(file_size_mb):
    tpb.update(chunk_size_mb)
    tpb.show()
    sleep(1)  # Simulate download time

tpb.stop()
print("Download complete!")
```

**Output:**
```plaintext
Downloading file...
[##########          ] 50.0%
[##############################] 100.0%
Download complete!
```

---

### Example 7: Nested Progress Bars
You can use multiple progress bars to represent nested tasks, such as downloading multiple files.

```python
from time import sleep

# Simulate downloading 3 files
num_files = 3
file_size_mb = 10
chunk_size_mb = 1

for file_num in range(1, num_files + 1):
    print(f"Downloading file {file_num}...")
    tpb = progressbar(filled="#", empty_char=" ", total=file_size_mb, size=30)

    for i in range(file_size_mb):
        tpb.update(chunk_size_mb)
        tpb.show()
        sleep(0.5)  # Simulate download time

    tpb.stop()
    print(f"File {file_num} downloaded!\n")

print("All files downloaded!")
```

**Output:**
```plaintext
Downloading file 1...
[##############################] 100.0%
File 1 downloaded!

Downloading file 2...
[##############################] 100.0%
File 2 downloaded!

Downloading file 3...
[##############################] 100.0%
File 3 downloaded!

All files downloaded!
```
