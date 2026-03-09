---
title: Installation
description: "How to install and set up Xeno Bot with all required dependencies."
tags:
  - installation
  - getting-started
  - setup
  - requirements
  - guide
keywords:
  - Installation
  - Setup
  - Getting Started
  - Dependencies
  - Node.js
author: Devvyyxyz
image:
date: 2026-03-09
permalink: /installation/
toc: true
icon: material/package
---

This guide covers the installation and setup of Xeno Bot, including dependency installation and environment preparation. Follow the steps below to get started.

---

## Prerequisites

Before installing Xeno Bot, confirm that your system meets the following requirements:

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Node.js**: Version 18 or later  
  !!! warning
      Ensure you have Node.js installed. Older versions may not support the latest `discord.js` features.  
      [Download Node.js here](https://nodejs.org/).
- **npm**: Comes bundled with Node.js 
- **Git**: Required for cloning the repository.  
  [Download Git here](https://git-scm.com/).

### Optional:
- **SQLite or Postgres**: SQLite is used by default for smaller setups. For larger deployments, install [PostgreSQL](https://www.postgresql.org/).

---

## Step 1: Clone the Repository

Open a terminal and run the following:
```bash
git clone https://github.com/devvyyxyz/xeno-bot.git
cd xeno-bot
```

!!! note
    Cloning the repository ensures you’re working with the latest stable Xeno Bot version. Keep your local copy updated by pulling new changes as needed.

---

## Step 2: Install Dependencies

Install the required dependencies by running:
```bash
npm install
```

This will set up everything listed in the `package.json` file.

!!! tip
    If you encounter errors during installation, make sure your Node.js version meets the requirements and your internet connection is stable. Use `npm install --legacy-peer-deps` if dependency conflicts occur.

---

## Step 3: Set Up the Environment

### Create a `.env` File

Copy the template environment file:
```bash
cp .env.example .env
```

Edit the `.env` file to include your bot token and other essential values. Example:
```env
TOKEN=your-bot-token
CLIENT_ID=your-client-id
GUILD_ID=123456789012345678 # Optional for development
LOG_LEVEL=info
```

!!! warning
    Never share your `.env` file or commit it to version control! Use `.gitignore` to ensure it stays local.

---

## Step 4: Verify Configuration Files

Xeno Bot requires configuration files in `config/`. Verify that the following files exist:
- `config/config.json`: General bot settings (e.g., prefix, owner). Example:
  ```json
  {
    "prefix": "!",
    "owner": "YOUR_USER_ID"
  }
  ```
- `config/bot.public.json`: Public bot metadata.
- `config/bot.dev.json`: Development-specific settings.

!!! note
    For detailed configuration steps, see the [Configuration Guide](/configuration/).

---

## Step 5: Run the Bot

Start the bot to ensure everything works as expected.

### Development Mode
Run the bot locally for development:
```bash
npm run start:dev
```

### Production Mode
Run the bot for public hosting:
```bash
npm start
```

!!! note
    Use `LOG_LEVEL=debug` in the `.env` file during development for detailed logging.

---

## Troubleshooting Installation Issues

Here are some common issues and solutions if you encounter problems during installation:

### Issue: "Command Not Found"
**Solution**: Make sure `npm` and `git` are added to your system’s PATH. Reinstall from [Node.js](https://nodejs.org/) or [Git](https://git-scm.com/) as needed.

### Issue: Dependency Errors
**Solution**: Use the following commands:
```bash
npm install --force
npm install --legacy-peer-deps
```

### Issue: Missing `.env` Variables
**Solution**: Double-check that the `.env` file exists and is properly configured. Refer to the [Configuration Guide](/configuration/) for details.

!!! tip
    For more issues, visit the [Deployment Guide](/deployment/) or join our community for assistance.

---

## Optional Step: Testing with Docker

Xeno Bot also supports Docker for simplified setup in containerized environments.

### Docker Quick Start
1. Build the Docker image:
   ```bash
   docker build -t xeno-bot .
   ```
2. Run the container:
   ```bash
   docker run -d --name xeno-bot xeno-bot
   ```

### Docker-Compose Example
Alternatively, use `docker-compose` for easier management:
```yaml
version: "3.9"
services:
  xeno-bot:
    build:
      context: .
    env_file:
      - .env
    ports:
      - "3000:3000"
    restart: unless-stopped
```

!!! tip
    For more advanced deployments, see the [Deployment Guide](/deployment/).

---

## Example Commands

Here are useful commands you may need during installation or development:

### Start the Bot
```bash
npm start
```

### Run with Debug Logs
```bash
LOG_LEVEL=debug npm start
```

### Deploy Slash Commands
```bash
npm run deploy-commands
```

---

## Helpful Links

- [Node.js Download](https://nodejs.org/)
- [Git Download](https://git-scm.com/)
- [Configuration Guide](/configuration/)
- [Deployment Guide](/deployment/)
- [GitHub Repository](https://github.com/devvyyxyz/xeno-bot)

---

With this guide, Xeno Bot should now be installed and ready for development or deployment. If you encounter any issues, refer to the troubleshooting section or reach out to the community.
```

---

### Features of this Page:
1. **Refined Structure**: Includes prerequisites, step-by-step instructions, and troubleshooting tips.
2. **Use of MkDocs Material Notes**: Added `!!! note`, `!!! tip`, and `!!! warning` to highlight critical details.
3. **Links to Relevant Pages**: Links to the Configuration and Deployment guides for seamless navigation.
4. **Docker Option**: An optional testing section for users familiar with Docker.
5. **Common Commands**: Added a quick reference for useful commands.

This installation page ensures everything is explained clearly for both novice and experienced users. Let me know if you require further changes or additions!