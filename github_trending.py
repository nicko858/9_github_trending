import requests
from requests import Timeout
from requests import ConnectionError
from datetime import date
from datetime import timedelta


def get_trending_repositories(api_url, top_size, period):
    date_to = date.today()
    date_from = date_to - timedelta(days=period)
    method = "search/repositories"
    target_url = "{}{}".format(api_url, method)
    parameters = {
        'q': ("created:{}..{}".format(date_from, date_to)),
        'per_page': top_size,
        'sort': 'stars'
        }
    response_code_ok = 200
    try:
        response = requests.get(target_url, params=parameters)
        if response.status_code != response_code_ok:
            raise ConnectionError
        return response.json()['items']
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


def get_total_open_issues_amount(repo):
    return repo["open_issues"]


def print_delimiter(count):
    delimiter = "*" * count
    print(delimiter)


def get_only_open_issues_amount(
        api_url,
        repo_owner,
        repo_name,
        total_open_issues_count
):
    method = "repos/{}/{}/issues".format(repo_owner, repo_name)
    target_url = "{}{}".format(api_url, method)
    parameters = {'per_page': total_open_issues_count, 'state': 'open'}
    response_code_ok = 200
    try:
        response = requests.get(target_url, params=parameters)
        if response.status_code != response_code_ok:
            raise ConnectionError
    except (Timeout, ConnectionError):
        return None
    issues_count = 0
    for issue in response.json():
        if 'pull_request' not in issue:
            issues_count += 1
    return issues_count


def extract_data_from_repo(repo):
    try:
        issues_and_pull_requests_count = (get_total_open_issues_amount
                                          (repo))
        repo_name = get_repo_name(repo)
        repo_url = get_repo_url(repo)
        repo_owner = get_repo_owner(repo)
        stars = get_stars_count(repo)
        issues_amount = get_only_open_issues_amount(
            api_url,
            repo_owner,
            repo_name,
            issues_and_pull_requests_count
        )
        if issues_amount is None:
            return None
    except (ValueError, KeyError, TypeError):
        return "Invalid data returned! Check input parameters!"
    return {
        "repository_name": repo_name,
        "repository_url": repo_url,
        "repository_owner": repo_owner,
        "stars_amount": stars,
        "open_issues_amount": issues_amount
    }


def print_title(title_was_printed):
    if not title_was_printed:
        print("\nThe most trending github repositories"
              " for the last week:\n")


def print_repo_data(repo_data):
    print_delimiter(90)
    for repo_item_name, repo_item_value in repo_data.items():
        print("{}: {}".format(repo_item_name, repo_item_value))


if __name__ == "__main__":
    api_url = "https://api.github.com/"
    top_size = 20
    trending_repos = get_trending_repositories(
        api_url,
        top_size,
        period=7
    )
    if not trending_repos:
        exit("The service '{}' is unavailable!".format(api_url))
    title_was_printed = False
    for repo in trending_repos:
        repo_data = extract_data_from_repo(repo)
        if not repo_data:
            exit("The service '{}' is unavailable!".format(api_url))
        if not isinstance(repo_data, dict):
            exit(repo_data)
        print_title(title_was_printed)
        title_was_printed = True
        print_repo_data(repo_data)



