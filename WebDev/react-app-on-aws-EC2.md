# 🚀 Deploy a React App to AWS EC2 (Beginner Guide)

This tutorial will walk you through deploying your React app to an EC2 instance and optionally adding a domain + SSL certificate.

---

## 🔐 Step 1: Log in to Your EC2 Instance

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

---

## ⚙️ Step 2: Update the System

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🟩 Step 3: Install Node.js (LTS Version)

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

---

## 🌐 Step 4: Install Nginx

```bash
sudo apt install nginx -y
```

---

## 🔐 Step 5: Install Certbot (SSL Tool)

```bash
sudo apt install certbot python3-certbot-nginx -y
```

---

## 📦 Step 6: Clone and Build Your React App

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
npm install
npm run build
```

---

## 📁 Step 7: Move Build Files to Web Directory

```bash
sudo mkdir -p /var/www/[app-name]
sudo cp -r dist/* /var/www/[app-name]/
```

> Replace `[app-name]` with your actual app name (e.g. `zentronix`)

---

## 🌐 Step 8: Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/[app-name]
```

### 👉 If you **have a domain**, paste this:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    root /var/www/[app-name];
    index index.html;

    location / {
        try_files $uri /index.html;
    }
}
```

### 👉 If you **don’t have a domain**, paste this:

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    root /var/www/[app-name];
    index index.html;

    location / {
        try_files $uri /index.html;
    }
}
```

---

## 🔗 Step 9: Enable Your Nginx Config

```bash
sudo ln -s /etc/nginx/sites-available/[app-name] /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🌍 Step 10: Point Your Domain to EC2 (If Applicable)

In your domain provider (like GoDaddy, Namecheap, etc.), set:

* A Record for `@` → your EC2 **public IP**
* A Record for `www` → your EC2 **public IP**

---

## 🔐 Step 11: Add Free SSL Certificate (Let’s Encrypt)

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

When prompted:

* ✅ Enter your email
* ✅ Agree to terms
* ✅ Choose **redirect HTTP to HTTPS**

---

## ✅ Optional: Check SSL Renewal Timer

```bash
sudo systemctl status certbot.timer
```

Certbot auto-renews your SSL cert every 60 days.

---

## 🎉 Done!

Now your site is live at:

* IP: `http://your-ec2-public-ip` (no domain)
* Domain: `https://yourdomain.com` (with SSL)