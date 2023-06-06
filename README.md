# Script to Automatically Import Goodnotes Files from Terminal

## Instructions

Create a file named `.env` and add the following information:

```
GMAIL_USER=YOUR_GMAIL
GMAIL_PASSWD=YOUR_GMAIL_PASSWORD
GOODNOTES_MAIL=YOUR_GOODNOTES_MAIL
EXPORT_DIR=YOUR_EXPORT_DIR
```
> Your password should be an [app password](https://support.google.com/accounts/answer/185833?hl=en).

Ensure the following `pip` dependencies are installed:

- `dotenv`
- `email`
