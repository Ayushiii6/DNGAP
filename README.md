This guide explains how to set up the code, install them, and run the code.

---

## Prerequisites
- Ensure you have **Python 3.8 or higher** installed on your system. You can check your Python version by running:
  ```bash
  python --version
  ```

### Step 1: Create a Virtual Environment (Optional but Recommended)
It’s best to create a virtual environment to avoid conflicts with system-level packages.

Create a virtual environment:

```bash
python -m venv myenv
```

#### Activate the virtual environment:

On Windows:

```bash
myenv\Scripts\activate
```

On macOS/Linux:

```bash
source myenv/bin/activate
```

### Step 2: Create requirements.txt File
Create a file named requirements.txt in your project directory and copy the following content into it:

```plaintext
pandas==1.5.3
numpy==1.23.5
matplotlib==3.7.1
seaborn==0.12.2
plotly==5.15.0
tensorflow==2.13.0
scikit-learn==1.3.1
ipython==8.16.0
```

### Step 3: Install Libraries
Navigate to the directory containing requirements.txt.

Install the libraries by running:
```bash
pip install -r requirements.txt
```

This command will install all the libraries with the specified versions.

### Step 4: Verify the Installation
You can verify the installation of the libraries by importing them in Python. Run the following commands in a Python interpreter or script:

```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc
from IPython.display import clear_output

print("All libraries imported successfully!")
```
If there are no errors, your environment is correctly set up.

### Step 5: Run Your Code
Once the libraries are installed and verified, you can run your Python IPYNB file using basic Jupyter Notebook Commands

