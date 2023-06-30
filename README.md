# Discord-token-checker
**Sorts all tokens into categories (Email verified, phone verified, unclaimed, unverified, full verified)**

# How To Run?
> 1. **Clone / download this repository.** <br />
>2. **Run pip install -r requirements.txt.** <br />
>3. **Put proxies in proxies.txt, format: username:password@host:port or ip:port if you wish to use proxies.** <br />
>4. **Put tokens in tokens.txt.** <br />
>5. **Run python main.py.**


```IV | Invalid | The token is invalid, it does not work``` <br />
```UC | Unclaimed | The token does not have an email or a phone linked``` <br />
```UV | Unverified | The token has an email linked, but it is not verified, it does not have a phone linked``` <br />
```EV | Email Verified | The token has an email linked that is verified, it does not have a phone linked``` <br />
```PV | Phone Verified | The token has an email linked, but it is not verified, it has a phone linked and verified``` <br />
```FV | Full Verified | The token has both an email and a phone linked and verified``` <br />
