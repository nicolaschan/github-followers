# GitHub Followers Graph
Ever wondered what the graph of users that you are following or are following you on GitHub looks like? Using the GitHub API, this simple Python script will answer this question!

## Examples
![graph example 1](https://i.imgur.com/k3phYdU.jpg)
![graph example 2](https://i.imgur.com/lnTkZ5C.jpg)

## Usage
You'll have to edit the source code for this one, but it's such a simple script that this shouldn't be a problem.

Inside `followers.py`, add your username and password in the `auth` variable like so:
```py
auth = ('your_username', 'your_password')
```
Adjust the user you are focused on and the depth of search. For your own good, keep depth relatively low (maximum I use is 3).
```py
add_connections('username', G, depth=2)
```
