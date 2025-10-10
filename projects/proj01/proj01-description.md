# Project 1: Reproducibility in Climate Studies

* **Statistics 159/259, Fall 2025**
* **Due 10/23/2025, 11:59PM PT**
* Prof. F. Pérez, GSI J. Butler, and GSI S. Andrade, Department of Statistics, UC Berkeley.
* This assignment is worth a maximum of **50 points**.
* Assignment type: **group homework assignment**

The assignment content is located in `hw03-climate.ipynb`.

**Deliverables:** For this assignment, you will have a single GitHub repository for your group. Your repository should contain the following:

- One notebook PER QUESTION in the assignment notebook that includes code to create the plots and simulations the question asks for, along with your written responses and discussion. Please remember to use markdown headings for each section/subsection so the entire notebook document is readable. All figures should be both rendered in the notebook and saved in a separate folder called `outputs`.

- Complete the contribution statement in `contribution_statement.md`, briefly and qualitatively detailing eahc group member's contributions to the assignment.

- An `ai_documentation.txt` file where your group will put any prompts and output from AI companions.

There are two parts to this homework:

1. Reproducing the lecture result using the Mauna Loa CO2 data (Questions 1-3).
2. Reproducing Figures 1-3 in [this paper](https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2016GL071039) (Questions 4-6).

We have provided you with the Matlab code that was used to generate such figures, in the `matlab` folder. This may help you as a guide for running the analysis, but it is not expected that you use the Matlab code as a template for yours.

The total grade for this homework is divided between:
- [15 Points] The Manua Loa CO2 Data. 
- [30 Points] The West Coast Heat Wave.
- [5 Points] Project Structure. See next section for mode details


When running your analyses and making plots, it may be useful to save `xarray` datasets as `netcdf` files and then read them in order to make just the plots. You can do this with [xarray.Dataset.to_netcdf](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.to_netcdf.html).

### Project Structure

In this homework we are going to evaluate your overall workflow using git and GitHub. Be sure that you repository includes clear commit messages as you make progress on the homework, and not include any other file or folder that those needed for the project. To ensure that extraneous files are ignored by git, we have added a `.gitignore` where you can either specify single files, or all files with a particular file extension. Additionally, the code in each notebook must be well organized. Use different cells for different operations and functions and markdown cells to explain the analysis. You can also use different branches or make a fork of the main repository (and then a pull request) in order to work collaboratively on the same notebook.

You will have to divide the notebook `hw03-climate.ipynb` into six different notebooks, one for each question. Name each one of these notebooks `climate-QXX.ipynb`, with `XX` corresponding to the number of the question (eg, `climate-Q02.ipynb`). You will have to move the code from `hw03-climate.ipynb` to each notebook in such a way that each notebook can be executed. You will have to take a look at which imports to make and what data to read in each notebook. For the final deliverable, remove the notebook `hw03-climate.ipynb` from the repository. Also, please include the `ai_documentation.txt` file.


**Acknowledgment:** Large part of the contents in this homework assignment were done by [Dr. Chelle Gentemann](https://cgentemann.github.io).