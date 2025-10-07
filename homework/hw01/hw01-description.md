# Homework 1 - Reproducibility checkup on an existing paper

* **Statistics 159/259, Fall 2025**
* **Due Thursday 9/18/2025, 11:59PM PT**
* This assignment is worth a maximum of **40 points**.
* Assignment type: **individual**.

As this [2016 Nature survey](https://www.nature.com/articles/533452a.pdf) points out,
*more than 70% of researchers have tried and failed to reproduce another
scientist’s experiments, and more than half have failed to reproduce
their own experiments*. Do you believe in every paper you read?

For this assignment we will ask you to identify a paper you find
interesting and evaluate how reproducible it is, *from a computational
perspective*. We will not focus on questions regarding experimental
replication, lab protocols, etc.

This could include (but it is not limited) to a paper of your area of
research or interests, which potentially introduces new methodology,
runs interesting experiments or just draws conclusions from previous
work. Don't worry if you don't have an active research area yet - below
we provide a starting list of potential papers you can use, pick one
that looks interesting to you.

As a proof of concept, try to pick a paper that in principle looks
reproducible. Evaluate the paper in the following categories. For each
one of the categories, we give you a series of questions that you can
check, but we also encourage you to think about other aspects if you feel inclined.

-   **Data Availability**:

    -   Is the data used in the paper available? If so, is it open or under request?
    -   What is the format of the data? How would you retrieve the data?
    -   Is it necessary to do any pre-processing to the data? If so, are the details for cleaning and pre-processing it explained and available?

-   **Software**:

    -   Do the authors provide or make reference to the software tools they used? Are these public or private? How reliable are they?
    -   If there is custom code written for the paper (not just using existing software packages), is it publicly available or _upon request_? (According to [Gabelica et al. (2022)](https://www.sciencedirect.com/science/article/pii/S089543562200141X), the chances to get the requested data are less than 10%).
    -   Do they use open source (e.g. Python, R, Julia) or proprietary programming languages (e.g. Matlab, Mathematica, IDL)?
    -   Do you think it will be easy to run their model? If so, is this because the analysis is intrinsically difficult or by lack of documentation?

-   **Analysis**:

    -   Do the authors provide a full description of the steps followed during the analysis?
    -   Is there any logical gap in the flow of data (eg, hyperparameter setting, cleaning or filtering of data)?

-   **Statistical Significance**:

    -   Is the net amount of data enough to lead to the conclusion/conclusions of the paper?
    -   Do the conclusions the authors claim follow directly from the analysis they do?
    -   Do the authors take into account uncertainties in the data they are using or in the methods they deploy to analyze the data? Are the results reported with error estimation?
    -   Do you think the conclusions may be biased towards what the authors want to prove instead of what the data suggest? After reading the paper, do you think the abstract actually reflects what the paper actually shows?

For each one of these four categories, you have to write a response of at least 200 words.
For further guidance about checkpoints for reproducibility, you can also
check [Joelle Pineau’s Reproducibility Checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf)
used in the NeurIPS Reproducibility Challenge. 

You will also have to write a response to the authors as if you were a referee who
just received this paper to be peer reviewed, as a _reproducibility
editor_. That is, you don't need to discuss the scientific merits or the
domain specific ideas in the paper, only focus on questions of
reproducibility.

-   Importantly, this response should be framed as a polite, constructive critique: imagine sending this to a colleague who will read it, where you are evaluating how well they did in this regard, and suggesting how they could improve.

-   In your response, make it as clear as possible which aspects of reproducibility are not satisfactory or missing and make suggestions about how the authors can improve the reproducibility of their work. The response has to be elaborated and well articulated. A good response is expected to be between 400 and 600 words.

We encourage you to find papers in your area of interest and/or research, but you can also start by looking at the following list of papers:

-   [https://github.com/jupyter/jupyter/wiki#reproducible-academic-publications](https://github.com/jupyter/jupyter/wiki#reproducible-academic-publications)
-   [https://github.com/leipzig/awesome-reproducible-research](https://github.com/leipzig/awesome-reproducible-research)
-   For a list of ML papers, you can check the list of [2019 NeurIPS accepted papers](https://reproducibility-challenge.github.io/neurips2019/task/), which were used during the Reproducibility Challenge.

# Deliverables

1.  Write out your answers by filling out the provided markdown file, according to the description above.

2.  Convert the markdown file to PDF using the [pandoc program](https://pandoc.org) (which is installed in the hub). To do this, you will need to run `pandoc hw01-response.md -o hw01-response.pdf` in your terminal, and the pdf file should appear. Commit this PDF also to your repository.

3.  Fill out the [Google Form](https://forms.gle/YM5CGTQN1uT8joZ19) (you can copy and paste from the full-form response in Markdown). Grade from poor (1) to good (5) how reproducible the paper is for each one of the evaluation categories above.