---
title: Deployment
description: "Deployment patterns: single host, sharded, Docker, and CI notes."
tags:
  - development
  - self-hosting
  - deployment
  - installation
keywords:
  - Deployment
  - Self hosting
  - Hosting
  - Running
  - Yaml
author: Devvyyxyz
image:
date: 2026-03-04
permalink: /deployment/
toc: true
icon: material/server
aliases:
  - /deploying/
---

# Deployment Guide

Deploying Xeno Bot is a straightforward process, with flexible options for both small-scale and large-scale setups. This guide will walk you through recommended deployment patterns, hosting services, and additional resources for seamless operation.

---

## Prerequisites

Before deploying Xeno Bot, ensure you have completed the following steps:
1. **Configure the Bot**: Follow the [Configuration Guide](/Self-Hosting/Configuration/) to set up your environment variables and JSON configuration files.
2. **Install Dependencies**: See the [Installation Page](/Self-Hosting/installation/) for instructions on installing the required packages and tools.

!!! note
    Proper configuration and installation are critical for a successful deployment. Ensure all prerequisites are met before proceeding.

---

## Deployment Options

Xeno Bot supports multiple deployment patterns depending on your requirements and resources. Choose the method that aligns with your use case:

### Single-Host Deployment

The simplest deployment method is running Xeno Bot on a single machine or server.

**Steps:**
1. SSH into your server.
2. Clone your Xeno Bot repository:
   ```bash
   git clone https://github.com/devvyyxyz/xeno-bot.git
   cd xeno-bot
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Set environment variables as needed (e.g., in a `.env` file).
5. Start the bot:
   ```bash
   npm start
   ```

!!! tip
    Single-host deployment is ideal for small communities or testing purposes. VPS providers such as [DigitalOcean](https://www.digitalocean.com/), [Linode](https://www.linode.com/), and [Vultr](https://www.vultr.com/) offer affordable and reliable hosting solutions.

---

### Sharded Deployment

For larger servers or communities, sharding can help distribute the bot's workload. This is particularly beneficial for bots managing multiple Discord guilds.

1. Ensure your bot has sharding logic. If you're using the default `discord.js` framework, it comes with built-in support for sharding.
2. Update the bot’s sharding logic in `src/index.js` or the entry point.
3. Use the `ShardingManager` in production:
   ```bash
   node src/index.js --sharded
   ```

!!! warning
    Sharded deployment should only be used if your bot is growing rapidly. Ensure that your hosting environment can handle the increased resource demands.

---

### Docker Deployment

Deploying Xeno Bot via Docker is a robust option for containerized environments.

**Steps:**
1. Create a `Dockerfile` for Xeno Bot:
   ```dockerfile
   FROM node:18-alpine
   WORKDIR /usr/src/xeno-bot
   COPY package*.json ./
   RUN npm install
   COPY . .
   CMD ["npm", "start"]
   ```
2. Build and run your Docker image:
   ```bash
   docker build -t xeno-bot .
   docker run -d --name xeno-bot xeno-bot
   ```
3. Use `docker-compose.yml` for advanced setups:
   ```yaml
   version: '3.8'
   services:
     bot:
       build: .
       env_file:
         - .env
       volumes:
         - .:/usr/src/xeno-bot
       ports:
         - "3000:3000"
       restart: unless-stopped
   ```

!!! note
    This method is excellent for larger teams or container orchestration platforms like Kubernetes.

Recommended hosting providers with Docker support:
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Heroku](https://heroku.com/) *(free tier available for smaller projects)*

---

### Continuous Integration (CI) Deployment

For automated and repeatable deployments, use CI/CD pipelines:

1. **Choose a CI/CD Platform**:
   - [GitHub Actions](https://github.com/features/actions)
   - [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
   - [CircleCI](https://circleci.com/)

2. **Example GitHub Actions Workflow**:
   ```yaml
   name: Deploy Xeno Bot
   on:
     push:
       branches:
         - main
   jobs:
     build-and-deploy:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Node.js
           uses: actions/setup-node@v3
           with:
             node-version: 18

         - name: Install dependencies
           run: npm install

         - name: Deploy bot
           run: npm start
   ```

!!! tip
    Combine CI/CD deployment with Docker for maximum automation and scalability.

---

## Recommended Hosts for Deployment

Here are some reliable hosting platforms to consider for deploying Xeno Bot:

- **Small-Scale Deployments**:
  - [DigitalOcean](https://www.digitalocean.com/) *(Affordable, beginner-friendly)*
  - [Linode](https://www.linode.com/) *(Scalable for small projects)*

- **Mid-Scale Deployments**:
  - [Heroku](https://www.heroku.com/) *(Great for CI/CD and Docker-based workflows)*
  - [Vultr](https://www.vultr.com/) *(Cost-effective with solid performance)*

- **Large-Scale Deployments**:
  - [AWS EC2](https://aws.amazon.com/ec2/) *(Highly scalable but complex)*
  - [Google Cloud](https://cloud.google.com/compute) *(Enterprise-level hosting)*
  - [Azure](https://azure.microsoft.com/) *(Reliable for corporate-level scaling needs)*

!!! note
    Consider your budget and technical expertise when selecting a hosting provider.

---

## Additional Resources

- [Configuration Guide](/Self-Hosting/Configuration/): Learn about environment variables and JSON configuration files.
- [Installation Guide](/Self-Hosting/installation/): Step-by-step instructions for installing Xeno Bot and its dependencies.

For help with specific issues, consult the [Troubleshooting section](installation.md#troubleshooting-installation-issues) of the Installation guide or join our community.

---

By choosing the deployment pattern that suits your needs and following best practices, you can ensure Xeno Bot is reliably hosted and scales with your community.