import requests
from requests import Timeout
from requests import ConnectionError
from datetime import date
from datetime import timedelta
import json
from json import JSONDecodeError


def get_trending_repositories(api_url, top_size, interval_a, interval_b):
    method = "search/repositories"
    query = "created:{}..{}".format(interval_b, interval_a)
    target_url = ("{}{}?q={}&sort=stars&per_page={}".format(
        api_url,
        method,
        query,
        top_size
    ))
    try:
        response = requests.get(target_url)
        return response.text
    except (Timeout, ConnectionError):
        return None


def get_stars_count(repo):
    return repo["stargazers_count"]


def get_repo_name(repo):
    return repo["name"]


def get_repo_owner(repo):
    return repo["owner"]["login"]


def get_repo_url(repo):
    return repo["html_url"]


def get_repo_open_issues_count(repo):
    return repo["open_issues"]


def make_data_to_print(repos):
    try:
        parsed_data = json.loads(repos)
        data_to_print = {}
        repos = parsed_data["items"]
        for repo in repos:
            repo_name = get_repo_name(repo)
            repo_url = get_repo_url(repo)
            repo_owner = get_repo_owner(repo)
            stars = get_stars_count(repo)
            open_issues_count = get_repo_open_issues_count(repo)
            data_to_print[repo_name] = [
                repo_owner,
                repo_url,
                stars,
                open_issues_count
            ]
        return data_to_print
    except JSONDecodeError:
        return None


def print_data(data_to_print, interval_a, interval_b):
    delimiter = "*" * 90
    print("\nThe most trending github repositories"
          " for the period from {} to {}:\n".format(
           interval_b,
           interval_a
          ))
    for repo_name, repo_info in data_to_print.items():
        print(delimiter)
        repo_url, repo_owner, stars, opened_issues_count = repo_info
        print("repo_name: {}\n"
              "repo_url: {}\nrepo_owner: {}\nstars: {}\n"
              "opened_issues_count: {}".format(
                  repo_name,
                  repo_url,
                  repo_owner,
                  stars,
                  opened_issues_count
              ))


if __name__ == "__main__":
    interval_a = date.today()
    interval_b = interval_a - timedelta(days=7)
    api_url = "https://api.github.com/"
    top_size = 20
    trending_repos = get_trending_repositories(
        api_url,
        top_size,
        interval_a,
        interval_b
    )
    if not trending_repos:
        exit("The service '{}' is unavailable!".format(api_url))
    data_to_print = make_data_to_print(trending_repos)
    if not data_to_print:
        exit("Invalid data returned! Check input parameters!")
    print_data(data_to_print, interval_a, interval_b)
