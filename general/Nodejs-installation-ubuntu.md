# Steps to Install Latest Node.js on Ubuntu

### 1. **Update your system**

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 2. **Install curl (if not already installed)**

```bash
sudo apt install curl -y
```

---

### 3. **Add NodeSource (Latest LTS or Current)**

#### 👉 For **Latest Stable LTS (Recommended for Production)**:

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```

#### 👉 For **Latest Current Version (e.g., 22.x)**:

```bash
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
```

---

### 4. **Install Node.js**

```bash
sudo apt install nodejs -y
```

This also installs `npm`.

---

### 5. **Verify installation**

```bash
node -v
npm -v
```

---

## ✅ Optional: Install `n` for Easier Version Switching (Advanced)

If you want to switch between multiple Node.js versions easily:

```bash
sudo npm install -g n
sudo n latest        # Or `n lts`
```

> You may need to restart your shell or use `sudo n latest` to use the new version immediately.

---
