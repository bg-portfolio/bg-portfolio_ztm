import requests
import hashlib
import sys
'''password checker from pwned API'''


def request_api_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    res = requests.get(url)
    if res.status_code != (200 or 202):
        raise RuntimeError(
            f"Error fetching: {res.status_code} check the API and try again")
    return res


def get_pass_leaks(hashes, hash_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, c in hashes:
        if h == hash_check:
            return c
    return 0


def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5)
    return get_pass_leaks(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times hacked")
        else:
            print(f"{password} was NOT found hacked")
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
