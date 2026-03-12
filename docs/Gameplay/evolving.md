---
title: Evolving
description:
tags:
keywords:
  - xeno
  - bot
  - documentation
author: Devvyyxyz
image:
date: 2026-03-04
permalink: /template/
toc: true
icon: material/file-document
aliases:
  - /template/
---
Xeno Bot's **evolution feature** allows you to progress your xenomorphs through their preset life cycle stages, like `Egg → Facehugger → Chestburster`, and beyond. Here’s everything you need to know about evolving your xenomorphs, the requirements, and how to manage active evolutions.

---

## How Evolution Works

Evolving a xenomorph requires meeting specific requirements, which vary depending on the stage. These requirements may include:
- **Cost**: Royal jelly (RJ), specific items, or hosts.
- **Time**: Evolutions take different amounts of time to complete. Be patient as your xenomorph grows.

### A Typical Evolution:
1. **Start an Evolution**:  
   Use the `/evolve` command to begin.
2. **Meet the Requirements**:  
   Ensure you have all the necessary resources, such as RJ, hosts, or items.
3. **Wait**:  
   Evolution is a timed process. You’ll receive a DM once it’s complete.

---

## Evolution Requirements

### Key Resources
1. **Royal Jelly (RJ)**:  
   A rare resource used in specific evolutions.
   
2. **Hosts**:  
   Typically required during the "Facehugger → next stage" evolution.  
   !!! warning
       Hosts are one-time use and consumed during the evolution process.

3. **Items**:  
   Certain items may be required for advanced evolution stages.  
   Check the bot's pathway with `/pathway` for details.

4. **Time**:  
   Evolution times vary by stage, ranging from a few minutes for basic stages to several hours for advanced ones.

---

## How to Start an Evolution

### Command:
To begin the evolution process, use the `/evolve` command:
```plaintext
/evolve
```

This command will guide you through selecting the xenomorph, showing its current stage, and displaying the requirements for its next evolution. Follow the bot's prompts to proceed.

---

## Managing Active Evolutions

Once an evolution starts, you can track its progress, cancel it, or view all active evolutions using `/evolve list`.

### Track Progress:
Command:
```plaintext
/evolve list
```

This command displays:
- The status of all your ongoing evolutions.
- Their estimated completion times.

### Cancel an Evolution:
If you decide to stop an evolution before it’s complete:
```plaintext
/evolve cancel
```
!!! tip
    Canceling an evolution refunds **some, but not all** of the resources used. Use this sparingly.

---

## Notifications for Evolution Completion

### DM Notifications:
As soon as an evolution is complete, Xeno Bot will send you a **direct message (DM)** letting you know that the process is finished and your xenomorph is ready.

### Channel Notifications:
The bot may also notify the Discord server (if enabled by the server admin) of significant evolution milestones.

---

## Evolution Path Overview

The evolution paths for xenomorphs are **preset**, meaning each xenomorph has a specific life cycle. Below is an example of the general xenomorph evolution flow:

1. **Egg**  
   → Facehugger  
2. **Facehugger**  
   → Requires a host (consumed during use)  
3. **Chestburster**  
   → Requires royal jelly or items  
4. **Next Stage(s)** (Depends on life cycle path for the specific xenomorph)

For detailed evolution paths, use `/pathway` or consult the [Support Server]().

---

## Troubleshooting Evolution

### Common Issues:
1. **Insufficient Resources**:  
   If you attempt an evolution without the required RJ, items, or hosts, Xeno Bot will notify you. Collect more resources and try again.

2. **No Hosts Available**:  
   Facehugger evolutions require hosts. Be sure to have hosts available in your inventory. New hosts can be obtained through `/hunt` or rewards.

!!! warning
    If evolutions are failing consistently, check with your server admin to ensure Xeno Bot is properly configured, or the [support server]().

---

## Strategies for Efficient Evolution

1. **Stock Up on Resources**:  
   Collect RJ, items, and hosts before starting evolutions to prevent delays.

2. **Time Management**:  
   Keep track of evolution times using `/evolve list` to know when to return and manage the next evolution.

3. **Optimize Hosts**:  
   Use hosts wisely, as they are consumed during Facehugger evolutions. Prioritize xenomorphs based on strategy and the resources required.

---

## Related Commands

Here are the evolution-specific commands:
- **Start an Evolution**:  
  ```plaintext
  /evolve
  ```
- **View Active Evolutions**:  
  ```plaintext
  /evolve list
  ```
- **Cancel an Active Evolution**:  
  ```plaintext
  /evolve cancel
  ```

---

Grow your xenomorph collection by mastering the evolution system. Ready to evolve your hive? Use `/evolve` and begin the transformation!