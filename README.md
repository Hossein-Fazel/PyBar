# PyBar: A Simple Python Progress Bar

**PyBar** is a lightweight and customizable progress bar implementation in Python. It is designed to be simple, flexible, and easy to integrate into your projects. Whether you're tracking the progress of a file download, data processing, or any other task, PyBar provides a clean and intuitive way to visualize progress.


## Features

- **Customizable Characters**: You can specify the characters used to represent filled and empty portions of the progress bar.
- **Adjustable Size**: The length of the progress bar can be adjusted to fit your needs.
- **Dynamic Updates**: The progress bar updates dynamically as the task progresses.
- **Progress Control**: You can start, update, and stop the progress bar as needed.
- **Unicode Support**: Use Unicode characters (e.g., █, ░, ⬛) for the filled and empty portions of the bar.
- **Multiple Display Formats**: Choose between full bar, percentage-only, or combined view

### Class Initialization

The `progressbar` class can be initialized with the following parameters:

- `filled` (str): The character used to represent the filled portion of the progress bar. Default is `"#"`.
- `empty_char` (str): The character used to represent the empty portion of the progress bar. Default is `" "` (space).
- `total` (int): The total number of steps required to complete the task. Default is `100`.
- `size` (int): The length of the progress bar in characters. Default is `50`.
- `start` (int): The starting point of the progress bar. Default is `0`.
- `display_mode` (str): Sets display format of progress bar, "full" (bar + percentage), "bar" (bar only), or "percent" (percentage only). Default is `full`


### Methods

- `reset()`: Resets the progress bar to its initial state.
- `update(value: int)`: Updates the progress bar by the specified value.
- `show()`: Displays the current state of the progress bar.
- `stop()`: Stops the progress bar and prints a new line.

---

## Usage

### Installation

PyBar can be installed in several ways:

#### Method 1: Install as a Python package (recommended)
You can now install PyBar directly using pip:

```bash
pip install git+https://github.com/Hossein-Fazel/PyBar.git
```

Or alternatively, after cloning the repository:

```bash
git clone https://github.com/Hossein-Fazel/PyBar.git
cd PyBar
pip install .
```


#### Method 2: Cloning the Repository

1. Clone the PyBar repository to your local machine:
   ```bash
   git clone https://github.com/Hossein-Fazel/PyBar.git
   ```

2. Navigate to the cloned directory:
   ```bash
   cd PyBar
   ```

3. copy the `PyBar` directory to your project

4. Import the progress bar in your Python script:
   ```python
   from PyBar.progressbar import ProgressBar
   ```

#### Method 3: Direct Download

1. Visit the GitHub repository at [https://github.com/Hossein-Fazel/PyBar](https://github.com/Hossein-Fazel/PyBar)

2. Click on the "Code" button and select "Download ZIP"

3. Extract the ZIP file and copy the `PyBar` directory to your project

4. Import it in your Python script:
   ```python
   from PyBar.progressbar import ProgressBar
   ```

### Requirements
PyBar has no external dependencies and works with:
- Python 3.6+
- Any operating system (Windows, Linux, macOS)

Once installed, you can start using PyBar immediately in your projects. The simple import statement gives you access to all the progress bar functionality shown in the examples above.

For the latest updates and bug fixes, you can periodically pull new changes from the repository:
```bash
git pull https://github.com/Hossein-Fazel/PyBar.git
```

### Basic Example

Here’s a simple example to get you started:

```python
from time import sleep

# Create a progress bar with default settings
tpb = ProgressBar()

# Simulate a task that takes 100 steps
for i in range(100):
    tpb.update(1)  # Update the progress bar by 1 unit
    tpb.show()     # Display the updated progress bar
    sleep(0.1)     # Simulate a delay

tpb.stop()  # Stop the progress bar and print a new line
```

**Output:**
```plaintext
[#########################                         ] 50.0%
[##################################################] 100.0%
```


### Customizing the Progress Bar

You can customize the progress bar by specifying the filled character, empty character, total steps, size, starting value and etc.

```python
# Create a custom progress bar
tpb = ProgressBar(filled="=", empty_char=".", total=100, size=50)

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


### Display modes

#### 1. Full Mode (Bar + Percentage)

```python
from time import sleep

pb = ProgressBar(display_mode="full")
for i in range(100):
    pb.update(1)
    pb.show()
    sleep(0.1)
pb.stop()
```
**Output:**
```
[#########################                         ] 50.0%
[##################################################] 100.0%
```

#### 2. Bar-Only Mode
```python
from time import sleep

pb = ProgressBar(display_mode="bar")
for i in range(100):
    pb.update(1)
    pb.show()
    sleep(0.1)
pb.stop()
```
**Output:**
```
[#########################                         ]
[##################################################]
```

#### 3. Percent-Only Mode
```python
from time import sleep

pb = ProgressBar(display_mode="percent")
for i in range(100):
    pb.update(1)
    pb.show()
    sleep(0.1)
pb.stop()
```
**Output:**
```
50.0%
100.0%
```


### Resetting the Progress Bar

You can reset the progress bar to its initial state using the `reset()` method.

```python
tpb = ProgressBar(total=100, size=50)

# Simulate a task
for i in range(50):
    tpb.update(1)
    tpb.show()
    sleep(0.1)

tpb.reset()  # Reset the progress bar

# Simulate another task
for i in range(100):
    tpb.update(1)
    tpb.show()
    sleep(0.1)

tpb.stop()
```

---

## Additional Examples

Some additional examples demonstrating various ways to use the `progressbar` class in different scenarios:

### Example 1: Custom Filled and Empty Characters
You can use different characters for the filled and empty portions of the progress bar.

```python
from time import sleep

# Create a progress bar with "=" as the filled character and "." as the empty character
tpb = ProgressBar(filled="=", empty_char=".", total=100, size=50)

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
tpb = ProgressBar(filled="#", empty_char=" ", total=100, size=20)

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
tpb = ProgressBar(filled="#", empty_char=" ", total=100, size=50, start=30)

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
tpb = ProgressBar(filled="#", empty_char=" ", total=10, size=20)

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
tpb = ProgressBar(filled="█", empty_char="░", total=100, size=40)

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
tpb = ProgressBar(filled="#", empty_char=" ", total=file_size_mb, size=30)

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
    tpb = ProgressBar(filled="#", empty_char=" ", total=file_size_mb, size=30)

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
