
TO use this code

(1) Create a file called keys.py.  In it, define four variables like this:

```
consumer_key='FAKE-VALUE-GO-GET-YOUR-OWN'
consumer_secret='FAKE-VALUE-GO-GET-YOUR-OWN'
access_token_key='FAKE-VALUE-GO-GET-YOUR-OWN'
access_token_secret='FAKE-VALUE-GO-GET-YOUR-OWN'
```

The real values will be strings such as `sd8ifjas9d8fjasdf` and you define them by following
the instructions here under "Create Your App".

https://python-twitter.readthedocs.io/en/latest/getting_started.html

Those instructions apply ONLY to getting the four magic values for the keys and secrets; the
rest of that documentation is for an entirely different library.

(2) Do:

```
pip3 install TwitterAPI
```

OR

```
pip install TwitterAPI
```

Depending whether you use `pip` or `pip3` to install things.

(3) Before running any code, do this:

```
export PYTHONIOENCODING=UTF-8
```

You need to do that in each terminal session before you run Python

(4) Run the code in `tryTwitter.py` with `python3 -i tryTwitter.py`

Good luck!

(5) Read the documentation to find out more about what you can do:

https://github.com/geduldig/TwitterAPI
