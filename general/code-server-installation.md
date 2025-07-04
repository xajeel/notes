# Code Server Installation on Server

## Requirements 
- Ubuntu Server
- Port 8080 open
- [Node js](https://nodejs.org/en)

## Commands

```bash
wget https://github.com/coder/code-server/releases/download/v4.9.1/code-server-4.9.1-linux-amd64.tar.gz

tar -xvf code-server-4.9.1-linux-amd64.tar.gz

cd code-server-4.9.1-linux-amd64/bin

```

**To run on Local Host**

```bash
./code-server
```

**To bind to any host**

```bash
./code-server --bind-addr 0.0.0.0:8080
```

