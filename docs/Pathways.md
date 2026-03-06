---
title: Xenomorph Pathways
description: Evolution pathways for xenomorphs in Xeno Bot
tags:
  - pathways
  - evolution
  - gameplay
keywords:
  - Xenomorph
  - Evolution
  - Pathways
  - Drone
  - Queen
author: Devvyyxyz
date: 2026-03-06
toc: true
icon: material/graph
---

# Xenomorph Pathways

This guide shows all evolution pathways for xenomorphs, from the initial egg/facehugger stage through to their final forms.

## Main Pathways

### Human Pathway (Standard)

The classic xenomorph evolution path using human hosts.

```mermaid
graph TD
    FH[Facehugger] -->|Human Host| D[Drone]
    D -->|10 Royal Jelly| W[Warrior]
    W -->|25 Royal Jelly| PR[Praetorian]
    PR -->|50 Royal Jelly| Q[Queen]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    classDef final fill:#702459,stroke:#4A1639,stroke-width:3px,color:#fff
    
    class FH start
    class D,W mid
    class PR advanced
    class Q final
```

| Stage | Requirements |
|-------|-------------|
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Drone | **Host:** ![Human](img/emojis/civilian.png){ width="24" } human |
| ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Drone → ![Warrior](img/emojis/warrior.png){ width="24" } Warrior | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 10 Royal Jelly |
| ![Warrior](img/emojis/warrior.png){ width="24" } Warrior → ![Praetorian](img/emojis/praetorian.png){ width="24" } Praetorian | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 25 Royal Jelly |
| ![Praetorian](img/emojis/praetorian.png){ width="24" } Praetorian → ![Queen](img/emojis/xenomorph_queen_sprite.png){ width="24" } Queen | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 50 Royal Jelly |

---

### Runner Pathway (Dog/Beast)

A faster, more agile pathway using animal hosts.

```mermaid
graph TD
    FH[Facehugger] -->|Beast Host| R[Runner]
    R -->|12 Royal Jelly| S[Sentry]
    S -->|30 Royal Jelly| C[Crusher]
    C -->|60 Royal Jelly| Q[Queen]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    classDef final fill:#702459,stroke:#4A1639,stroke-width:3px,color:#fff
    
    class FH start
    class R,S mid
    class C advanced
    class Q final
```

| Stage | Requirements |
|-------|-------------|
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Runner](img/emojis/runner.png){ width="24" } Runner | **Host:** dog, ox, bat, or snake |
| ![Runner](img/emojis/runner.png){ width="24" } Runner → ![Sentry](img/emojis/sentry.png){ width="24" } Sentry | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 12 Royal Jelly |
| ![Sentry](img/emojis/sentry.png){ width="24" } Sentry → ![Crusher](img/emojis/crusher.png){ width="24" } Crusher | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 30 Royal Jelly |
| ![Crusher](img/emojis/crusher.png){ width="24" } Crusher → ![Queen](img/emojis/xenomorph_queen_sprite.png){ width="24" } Queen | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 60 Royal Jelly |

---

### King Pathway (Royal)

The most powerful pathway, creating royal xenomorphs.

```mermaid
graph TD
    KF[King Facehugger] -->|30 RJ + Host| KN[Knight]
    KN -->|50 Royal Jelly| GD[Grand Duke]
    GD -->|75 Royal Jelly| P[Prince]
    P -->|120 Royal Jelly| K[King]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    classDef final fill:#702459,stroke:#4A1639,stroke-width:3px,color:#fff
    
    class KF start
    class KN mid
    class GD advanced
    class P,K final
```

| Stage | Requirements |
|-------|-------------|
| ![King Facehugger](img/emojis/facehugger.png){ width="24" } King Facehugger → ![Knight](img/emojis/warrior.png){ width="24" } Knight | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 30 Royal Jelly<br>**Host:** ![Human](img/emojis/civilian.png){ width="24" } human, ![Predator](img/emojis/predator.png){ width="24" } predator, or ![Engineer](img/emojis/engenieer.png){ width="24" } engineer |
| ![Knight](img/emojis/warrior.png){ width="24" } Knight → ![Grand Duke](img/emojis/praetorian.png){ width="24" } Grand Duke | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 50 Royal Jelly |
| ![Grand Duke](img/emojis/praetorian.png){ width="24" } Grand Duke → ![Prince](img/emojis/king.png){ width="24" } Prince | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 75 Royal Jelly |
| ![Prince](img/emojis/king.png){ width="24" } Prince → ![King](img/emojis/king.png){ width="24" } King | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 120 Royal Jelly |

---

### Deacon Pathway (Engineer)

A unique pathway creating the powerful Deacon xenomorph.

```mermaid
graph TD
    H[Hammerpede] -->|15 Royal Jelly| T[Trilobite]
    T -->|40 RJ + Engineer| D[Deacon]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef final fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class H start
    class T mid
    class D final
```

| Stage | Requirements |
|-------|-------------|
| ![Hammerpede](img/emojis/Hammerpede.webp){ width="24" } Hammerpede → ![Trilobite](img/emojis/Trilobite.jpg){ width="24" } Trilobite | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 15 Royal Jelly |
| ![Trilobite](img/emojis/Trilobite.jpg){ width="24" } Trilobite → ![Deacon](img/emojis/deacon.png){ width="24" } Deacon | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 40 Royal Jelly<br>**Host:** ![Engineer](img/emojis/engenieer.png){ width="24" } engineer |

---

### Neomorph Pathway

A separate evolution line starting from Neomorph eggs.

```mermaid
graph TD
    E[Neomorph Egg] -->|Hatch| BB[Bloodburster]
    BB -->|35 RJ + Human| N[Neomorph]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef final fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class E start
    class BB mid
    class N final
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Neomorph Egg → ![Bloodburster](img/emojis/chestburster.png){ width="24" } Bloodburster | Hatch the egg |
| ![Bloodburster](img/emojis/chestburster.png){ width="24" } Bloodburster → ![Neomorph](img/emojis/neomorph.png){ width="24" } Neomorph | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 35 Royal Jelly<br>**Host:** ![Human](img/emojis/civilian.png){ width="24" } human |

---

## Special Pathways

### Predalien Pathway

The hybrid xenomorph-predator evolution path, combining traits from both species.

```mermaid
graph TD
    PE[Predalien Egg] -->|Predator Host| PF[Predalien Facehugger]
    PF -->|Emerge| HB[Hybrid Chestburster]
    HB -->|35 Royal Jelly| PD[Predalien Drone]
    PD -->|45 Royal Jelly| PW[Predalien Warrior]
    PW -->|60 Royal Jelly| PB[Predalien Brute]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    classDef final fill:#702459,stroke:#4A1639,stroke-width:3px,color:#fff
    
    class PE start
    class PF,HB mid
    class PD,PW advanced
    class PB final
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Predalien Egg → ![Facehugger](img/emojis/facehugger.png){ width="24" } Predalien Facehugger | **Host:** ![Predator](img/emojis/predator.png){ width="24" } predator (obtained through hunts) |
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Predalien Facehugger → ![Chestburster](img/emojis/chestburster.png){ width="24" } Hybrid Chestburster | Automatic emergence |
| ![Chestburster](img/emojis/chestburster.png){ width="24" } Hybrid Chestburster → ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Predalien Drone | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 35 Royal Jelly |
| ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Predalien Drone → ![Warrior](img/emojis/warrior.png){ width="24" } Predalien Warrior | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 45 Royal Jelly |
| ![Warrior](img/emojis/warrior.png){ width="24" } Predalien Warrior → ![Brute](img/emojis/predalien.png){ width="24" } Predalien Brute | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 60 Royal Jelly |

---

### Spitter Pathway (Toxic)

Xenomorphs with potent acid-spitting abilities from toxic-exposed hosts.

```mermaid
graph TD
    CE[Classic Egg] -->|Toxic Host| FH[Facehugger]
    FH -->|Emerge| TC[Toxic Chestburster]
    TC -->|15 Royal Jelly| SD[Spitter Drone]
    SD -->|35 Royal Jelly| SW[Spitter Warrior]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class CE start
    class FH,TC mid
    class SD,SW advanced
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Classic Egg → ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger | **Host:** ![Toxic](img/emojis/black_goo.png){ width="24" } toxic-exposed human |
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Chestburster](img/emojis/chestburster.png){ width="24" } Toxic Chestburster | Automatic emergence |
| ![Chestburster](img/emojis/chestburster.png){ width="24" } Toxic Chestburster → ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Spitter Drone | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 15 Royal Jelly |
| ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Spitter Drone → ![Warrior](img/emojis/warrior.png){ width="24" } Spitter Warrior | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 35 Royal Jelly |

---

### Prowler Pathway (Agile)

Highly agile xenomorphs from feline or avian hosts, specialized for stealth.

```mermaid
graph TD
    CE[Classic Egg] -->|Agile Host| FH[Facehugger]
    FH -->|Emerge| MC[Micro Chestburster]
    MC -->|12 Royal Jelly| PD[Prowler Drone]
    PD -->|28 Royal Jelly| PA[Prowling Assassin]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class CE start
    class FH,MC mid
    class PD,PA advanced
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Classic Egg → ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger | **Host:** feline or birdlike |
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Chestburster](img/emojis/chestburster.png){ width="24" } Micro Chestburster | Automatic emergence |
| ![Chestburster](img/emojis/chestburster.png){ width="24" } Micro Chestburster → ![Drone](img/emojis/runner.png){ width="24" } Prowler Drone | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 12 Royal Jelly |
| ![Drone](img/emojis/runner.png){ width="24" } Prowler Drone → ![Assassin](img/emojis/runner.png){ width="24" } Prowling Assassin | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 28 Royal Jelly |

---

### Protomorph Pathway (Self-Evolving)

Ancient xenomorph variant that evolves without a host - self-contained evolution.

```mermaid
graph TD
    PE[Proto Egg] -->|Self-Evolve| PW[Protomorph Warrior]
    PW -->|40 Royal Jelly| EP[Elder Protomorph]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    
    class PE start
    class PW,EP mid
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Proto Egg → ![Warrior](img/emojis/xenomorph_sprite.png){ width="24" } Protomorph Warrior | **No host required** - self-evolves |
| ![Warrior](img/emojis/xenomorph_sprite.png){ width="24" } Protomorph Warrior → ![Elder](img/emojis/Xenomorph.png){ width="24" } Elder Protomorph | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 40 Royal Jelly |

**Special Note:** This pathway is unique - the Proto Egg does not need a host and evolves independently.

---

### Jockey Pathway (Engineer)

Elite xenomorphs from the rare Space Jockey eggs and engineer hosts.

```mermaid
graph TD
    SJ[Space Jockey Egg] -->|Engineer Host| FH[Facehugger]
    FH -->|Emerge| CB[Chestburster]
    CB -->|40 Royal Jelly| JD[Jockey Drone]
    JD -->|65 Royal Jelly| JS[Jockey Sentinel]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class SJ start
    class FH,CB mid
    class JD,JS advanced
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Space Jockey Egg → ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger | **Host:** ![Engineer](img/emojis/engenieer.png){ width="24" } engineer (rare event capture) |
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Chestburster](img/emojis/chestburster.png){ width="24" } Chestburster | Automatic emergence |
| ![Chestburster](img/emojis/chestburster.png){ width="24" } Chestburster → ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Jockey Drone | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 40 Royal Jelly |
| ![Drone](img/emojis/xenomorph_sprite.png){ width="24" } Jockey Drone → ![Sentinel](img/emojis/warrior.png){ width="24" } Jockey Sentinel | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 65 Royal Jelly |

**Special Note:** Engineer hosts are extremely rare and obtained through special capture events.

---

### Irradiated Pathway

Radioactive xenomorphs from radiation-exposed hosts with unique glowing properties.

```mermaid
graph TD
    IE[Irradiated Egg] -->|Rad-Exposed Host| FH[Facehugger]
    FH -->|Emerge| GB[Glowing Burster]
    GB -->|20 Royal Jelly| ID[Irradiated Drone]
    ID -->|40 Royal Jelly| IW[Irradiated Warrior]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class IE start
    class FH,GB mid
    class ID,IW advanced
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Irradiated Egg → ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger | **Host:** ![Radiation](img/emojis/atom.png){ width="24" } radiation-exposed human |
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Chestburster](img/emojis/chestburster.png){ width="24" } Glowing Burster | Automatic emergence |
| ![Chestburster](img/emojis/chestburster.png){ width="24" } Glowing Burster → ![Drone](img/emojis/Xenomorph.png){ width="24" } Irradiated Drone | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 20 Royal Jelly |
| ![Drone](img/emojis/Xenomorph.png){ width="24" } Irradiated Drone → ![Warrior](img/emojis/warrior.png){ width="24" } Irradiated Warrior | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 40 Royal Jelly |

---

### Berserker Pathway

Powerful brute-force xenomorphs from large bear-like hosts.

```mermaid
graph TD
    BE[Berserker Egg] -->|Large Host| FH[Facehugger]
    FH -->|Emerge| BB[Burster]
    BB -->|25 Royal Jelly| BD[Berserker Drone]
    BD -->|45 Royal Jelly| BW[Berserker Warrior]
    
    classDef start fill:#8B4513,stroke:#654321,stroke-width:3px,color:#fff
    classDef mid fill:#4A5568,stroke:#2D3748,stroke-width:3px,color:#fff
    classDef advanced fill:#2C5282,stroke:#1A365D,stroke-width:3px,color:#fff
    
    class BE start
    class FH,BB mid
    class BD,BW advanced
```

| Stage | Requirements |
|-------|-------------|
| ![Egg](img/emojis/egg.png){ width="24" } Berserker Egg → ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger | **Host:** bear-like (large creature) |
| ![Facehugger](img/emojis/facehugger.png){ width="24" } Facehugger → ![Chestburster](img/emojis/chestburster.png){ width="24" } Burster | Automatic emergence |
| ![Chestburster](img/emojis/chestburster.png){ width="24" } Burster → ![Drone](img/emojis/crusher.png){ width="24" } Berserker Drone | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 25 Royal Jelly |
| ![Drone](img/emojis/crusher.png){ width="24" } Berserker Drone → ![Warrior](img/emojis/warrior.png){ width="24" } Berserker Warrior | **Cost:** ![RJ](img/emojis/royal_jelly.png){ width="24" } 45 Royal Jelly |

---

## Host Types

Different hosts produce different xenomorph variants:

| Host Type | Produces | Used In |
|-----------|----------|---------|
| **Human** | Drone, Neomorph | Standard, King, Neomorph pathways |
| **Dog/Ox/Bat/Snake** | Runner | Runner pathway |
| **Predator** | Predalien | King pathway, Predalien pathway |
| **Engineer** | Deacon, Jockey | King, Deacon, Jockey pathways |
| **Toxic** | Spitter | Spitter pathway |
| **Feline/Bird** | Prowler | Prowler pathway |
| **Radiation-Exposed** | Irradiated | Irradiated pathway |
| **Bear-like (Large)** | Berserker | Berserker pathway |

---

## Tips

!!! tip "Resource Management"
    Royal Jelly is essential for evolution. Plan your evolution path carefully based on available resources.

!!! info "Host Rarity"
    Some hosts like Engineers and Predators are rare. Save special eggs until you have the appropriate host available.

!!! warning "Special Requirements"
    Some pathways have unique requirements - the Protomorph pathway doesn't need a host, while the Jockey pathway requires rare event captures.

!!! tip "More Information"
    For specific stat changes and abilities at each stage, see the [Encyclopedia command](Commands/Collection.md#encyclopedia).
