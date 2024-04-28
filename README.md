# smtp-mail-bot

Welcome to the Custom Domain SMTP Mail Bot Server! This self-hosted solution allows you to read email content from your custom domain, making it perfect for applications like verification bots. Below you'll find detailed instructions on setting up and running the server.

## Config

### 1. Prerequisites

- A custom domain (e.g. `devmailserver.xyz`)
- Access to your domain registrar's DNS settings (highly recommend [cloudflare](https://cloudflare.com/))
- Port forwarding configuration on your router (if running locally)

### 2. DNS Records Configuration

**A Record**

```sh
Type: A
Name: devmailserver.xyz
Content/Value: 123.123.123.123 (replace with your public IP address)
TTL: Automatic
```

**MX Record**

```sh
Type: MX
Name: devmailserver.xyz
Content/Value: devmailserver.xyz
Priority: 10
TTL: Automatic
```

### 3. Port Forwarding

Ensure that port `25` is forwarded to the private IP address of the machine where the server will run. Refer to your router's manual or online guides for port forwarding instructions.

### 4. Code

Within [smtp-mail-bot.py](smtp-mail-bot.py), configure the constants to your purposes (ie `DOMAIN`, `HOST`, `PORT`), and then run:

```sh
python smtp-mail-bot.py
```
