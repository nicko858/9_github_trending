# Github Trends

The script provides data of the most github's trending repositories for the last week.

# Quickstart

The program is represented by the module github_trending.py. Module github_trending.py contains the following functions:

- ```extract_data_from_repo()```
- ```get_only_open_issues_amount()```
- ```get_repo_name()```
- ```get_repo_owner()```
- ```get_repo_url()```
- ```get_stars_count()```
- ```get_total_open_issues_amount()```
- ```get_trending_repositories()```
- ```print_delimiter()```
- ```print_repo_data()```
- ```print_title()```

The program uses these libs from Python standart and third-party libraries:

```datetime```
```request```

**How in works:**

- The program connects to the https://github.com/ 
- Using ```search/repositories```- method, gets top-20 -data trending repositories of the last week (The trend repository has a lot of stars)
- Using ```list-issues``` - method to get opened issues
- Prints result in human-readble format  

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.


# How to run
- Activate virtualenv
``` bash
source <path_to_virtualenv>/bin/activate
```
- Run script with virtualenv-interpreter
```bash
<path_to_virtualenv>/bin/python3.5 github_trending.py
```
If everything is fine, you'll see such output:
```text
The most trending github repositories for the period from 2018-07-16 to 2018-07-23:

******************************************************************************************
repo_name: ru-web-developer-security-checklist
repo_url: minotaura
repo_owner: https://github.com/minotaura/ru-web-developer-security-checklist
stars: 84
opened_issues_count: 0
******************************************************************************************
repo_name: WanAndroid
repo_url: jenly1314
repo_owner: https://github.com/jenly1314/WanAndroid
stars: 98
opened_issues_count: 0
******************************************************************************************
```

In case of github unavaible, you'll see this message:
```text
The service https://api.github.com/ is unavailable!
```

In case of wrong data format, you'll see this message:
```text
Invalid data returned! Check input parameters!
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
