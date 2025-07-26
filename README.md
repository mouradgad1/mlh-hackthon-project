# Nexus Music - YouTube Music Streaming App

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)


## Overview

Nexus Music is a web application that allows users to search for and stream music from YouTube. The application consists of:
- Flask backend for handling search and streaming requests
- Frontend interface built with vanilla HTML/CSS/JavaScript
- yt-dlp integration for YouTube content extraction

## Features

- Search for songs, artists, or albums
- Stream music directly from YouTube
- Responsive design that works on desktop and mobile
- Audio player with play/pause, next, previous controls
- Progress bar and time display
- Volume control with mute functionality

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/nexus-music.git
cd nexus-music
```

### Step 2: Install Dependencies
Make sure you have Python 3.8+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
    ```bash
    python app.py
    ```
2. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. Use the search bar to find songs or artists and start streaming!

## Project Structure

```
app.py
requirements.txt
README.md
templates/
    index.html
```

- `app.py`: Main Flask application with API endpoints for search and streaming.
- `requirements.txt`: Python dependencies.
- `templates/index.html`: Frontend HTML, CSS, and JavaScript.

