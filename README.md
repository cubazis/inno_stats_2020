# Installation

1. Install [Python 3.9](https://www.python.org/downloads/).
1. In terminal change current working directory to the root of this repository.
1. (Optional) Initialize virtual environment and activate it according to the
   [tutorial](https://docs.python.org/3/library/venv.html).
1. Run `python -m pip install -U pip setuptools wheel`. This will update pip, setuptools and wheel packages.
1. Run `pip install -r requirements.txt`. This will install all necessary packages for the project.
1. If on Windows:
    - [Resolve](https://stackoverflow.com/a/65552261/14369408) notebook problems.
    - In environmental variables set ComSpec to PowerShell path.

# Dataset

The raw dataset consists of 9 different columns:

|   Column         | Description
|------------|--------------
| **date** | Timestamp when the purchase was done
| **id_doc** | Receipt's id
| **id_order** | Order's id. Order's id is equal to 0 when the purchase was done offline, otherwise online
| **id_card** | Unique id of customer
| **id_tov** | Unique id of product's id
| **id_kontr** | Distributor's id
| **quantity** | Amount of the same product in receipt which was purchased
| **sum** | Price of the product
| **is_green** | Shows that product is under discount or not
