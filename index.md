---
title: 'Stat 159 - Collaborative and Reproducible Data Science'
subtitle: 'UC Berkeley, Fall 2025'
---

::::{grid} 1 2 2 2
:::{card}
:header: **Fernando Pérez**

![Fernando Pérez](images/perez.jpg)

+++

* **Office Hours**: Mon 10am-11am (Evans 419); [Zoom session](https://berkeley.zoom.us/j/95027833312?pwd=c60W5ii4fypGD3TUo5GDo1aQL25xES.1) for those who need to join remotely.
* **Pronouns**: He/Him
* [fernando.perez@berkeley.edu](mailto:fernando.perez@berkeley.edu)
:::

:::{card}
:header: **Jimmy Butler**

![Jimmy Butler](images/butler.jpg)

+++

* **Office Hours**: Wed 1PM-2PM & Thur 10AM-11AM (Evans 428)
* **Pronouns**: He/Him
* [butlerj@berkeley.edu](mailto:butlerj@berkeley.edu)
:::

:::{card}
:header: **Sequoia Andrade**
![Sequoia Andrade](images/andrade.jpg)

+++

* **Office Hours**: Tues 1PM-2PM (Evans 428)
* **Pronouns**: She/Her
* [srandrade@berkeley.edu](mailto:srandrade@berkeley.edu)
:::

::::

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/site/HEAD)

This course teaches _the why and how_ of reproducible and collaborative research by combining questions of good computational practice in science, open science and statistical data analysis, in the context of today's research environment.  We will interleave practical topics in software engineering and statistical computing with broader discussions on elements of the
philosophy of science and the foundations of statistics.

From a domain perspective, we will use this course as an opportunity to learn about modern questions in one of today's most challenging problems for humanity: that of climate change and environmental damage to our planet. We will see how the tools and practices we learn in this course can contribute to tackling these problems.  We will also visit examples from other fields, including biomedical research, to broaden our perspective.

We will rely on the Scientific Python and Jupyter ecosystems, but the core ideas presented here can be equally implemented with tools in Julia, R, or any other programming language.

Consistent class participation is crucial: we will be discussing subtle substantive, technical, and philosophical issues and reviewing code during class. Even though we plan to record the lectures, if you cannot attend the lectures synchronously, please do *not* take the course.

There will be roughly 6-7 homeworks and 3 projects. The homeworks are to be completed individually, and projects will be collaborative in groups of 3-4. You will be asked to review your own contributions and each others contributions
to group projects.
There will not be a midterm or final exam, but there will be a videorecorded
final presentation of group work.

_Note:_ This course is inspired by, and based on, previous editions taught by myself as well as Professor Philip Stark, from UC Berkeley's Statistics Department. Much of the content and structure of the course was developed by [Facu Sapienza](https://statistics.berkeley.edu/people/facu-sapienza).

**Course Objectives:** At the completion of this course, students will:

1.  understand the issues regarding reproducible research in modern
    scientific practice, including the definitions of key concepts and
    the different challenges that exist across disciplines

2.  understand the computational and statistical issues involved with
    reproducibility

3.  be proficient at the Unix commandline

4.  be proficient at version control with Git

5.  be able to write documents in Markdown or LaTeX (including using
    pandoc)

6.  be familiar with scientific computing in Python

## Key Resources

+ Communication: [Ed Discussion](https://edstem.org/us/courses/84806/discussion) forum.

+ Lectures will be recorded and posted in the Kaltura system (visible via bCourses), but attendance is mandatory. (Much of the pedagogical value of the class is in participating in discussions and code reviews).

+ Course readings that are not easy to find free on the web or through the UC Berkeley Library will be posted to [bCourses](https://bcourses.berkeley.edu/).

+ Computing resources
    - We will use Jupyter notebooks. We will start with hosted notebooks on our [Stat 159 JupyterHub](https://stat159.datahub.berkeley.edu). Later in the term, we will discuss installing Jupyter on your own device. The JupyterHub server will have all the packages you need pre-installed.
    - The sources for class notes and most other materials are available [on github](https://github.com/UCB-stat-159-f25/site), with a rendered version [here](https://ucb-stat-159-f25.github.io/site).
    - Assignments should be submitted by pull request to your private repositories using the GitHub Classroom.
    - Whenever you need to work with GitHub, remember to activate GitHub authentication from the JupyterHub. The most convenient way to do this is to keep a notebook with just one cell like this:
    
```python
import gh_scoped_creds
%ghscopedcreds
```
    
You can also authenticate by running the command `gh-scoped-creds` at a terminal and following the instructions. If once authenticated you can't push to a given repo, it may be that you forgot to add that repo/org to your setup of the authentication app, go [here](https://github.com/apps/stat159-berkeley-datahub-access) to configure the app's permissions.

For your convenience, there is a notebook titled `GHAUTH.ipynb` in the `shared` folder, which does this. You can copy it to your home directory to use it further.

+ **A note on the Berkeley Library EZProxy:** Some of the resources listed here are scientific articles available only behind journal paywalls. If you haven't already, you should configure your web browser to use the campus [library EZProxy](https://guides.lib.berkeley.edu/ezproxy) so you can access them even if you are working from an off-campus network.
