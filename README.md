# SES and Behavior Game (oTree)

This repository contains the oTree implementation of a multi-game experimental suite designed to explore the effects of **social status (SES)** on prosocial behavior, developed for ECON 165 at UC Santa Cruz. The project idea originated from Kayson Tang, Victor Shi, and Chidalu Maduewesi.

This experiment investigates how visibility of social status influences behavior in three classic economic games:
- **Dictator Game**
- **Trust Game**
- **Prisoner's Dilemma**

Players first participate without SES information, and then repeat the games with SES information shown.

## 🧪 Experimental Structure
- Games are played in **pairs**, with random matching each round.
- Each block consists of a full cycle through all three games.
- Players complete two blocks: one **blind** to SES, one with **SES visible**.
- A Google Form survey is used pre-experiment to assign SES types.

## 📁 Repo Contents
- `ses_behavior/` — main oTree app with game logic
  - `models.py` — defines roles, payoffs, SES assignment
  - `pages.py` — controls game flow and logic across blocks
  - `templates/` — HTML templates for each page
- `settings.py` — oTree session configurations and app sequence
- `requirements.txt` — Python dependencies
- `Procfile` — for deployment on platforms like Heroku

---

## 🧩 How It Works

1. Players complete a short SES survey.
2. Players are randomly matched to play:
   - A Dictator Game
   - A Trust Game
   - A Prisoner’s Dilemma
3. After one full block, players are informed of their partner’s SES and repeat the cycle.
4. Payoffs are calculated based on game outcomes and shown in a final results page.

---

## 🔧 Customization

Settings in `settings.py` allow easy toggling:
- Change number of rounds per block
- Modify SES conditions
- Add/remove games in the `app_sequence`

---

## ▶️ Running the Game Locally

### 1. Clone the repository
```bash
git clone https://github.com/vivianzvz/ses_behavior.git
cd ses_behavior
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3.  Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the oTree dev server
```bash
otree devserver
```
