# pf-memer

## Overview

The **Meme Worthiness Analyzer** is a command-line tool that evaluates the meme potential of textual content and determines if it is suitable for launching a token on **pump.fun**. The tool utilizes OpenAI's **GPT-4o-mini** to analyze the provided text file and generate structured output with a **meme-worthiness score (1-10)** and token launch values.

## Features

- Supports **any text-based file format** (TXT, JSON, CSV, etc.).
- Assigns a **meme-worthiness score** from **1 to 10**.
- Suggests token attributes such as:
  - **Token name**
  - **Ticker**
  - **Description**
  - **Image/video meme idea**
  - **Social links (Telegram, Website, Twitter/X)**
- Outputs structured JSON for easy integration.

## Installation

### Prerequisites

- Python **3.12+**
- OpenAI API key

### Install Dependencies

```sh
pip install openai click
```

## Usage

### Running the Script

```sh
python pf_memer --api-key YOUR_OPENAI_API_KEY --file-path path/to/your/file.txt
```

### Example Input File

#### JSON

```json
{
  "text": "Why did the chicken cross the road? To buy the dip!",
  "likes": 12000,
  "retweets": 1500,
  "replies": 900,
  "verified_engagement": 350,
  "qrt_volume": 120
}
```

#### CSV or TXT

```txt
Elon Musk just tweeted "Doge to the moon!" 🚀
```

### Example Output

```json
{
  "meme_worthiness_score": 9,
  "name": "Doge to the Moon",
  "ticker": "DOGEMOON",
  "description": "Imagine thinking you can make it without riding this absolute gigachad of a coin. NGMI. Diamond hands only, no paper-handed plebs allowed.",
  "image_or_video_idea": "Elon Musk in a spacesuit with Doge on the moon, with a Wojak crying in the background as he misses out.",
  "telegram_link": "https://t.me/dogemoon",
  "website_link": "https://dogemoon.com",
  "twitter_x_link": "https://x.com/dogemoon"
}
```

## Notes

- The model determines meme-worthiness based on **absurdity, controversy, engagement, and virality potential**.
- The script enforces a structured JSON format for consistency.
- Results are dependent on the **quality and virality of the input text**.

## License

MIT License

## Author

Built for **meme enthusiasts & crypto traders** 🚀
