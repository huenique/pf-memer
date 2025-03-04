import json
from typing import Any

import click
import openai
from openai import OpenAIError


class MemeWorthyAnalyzer:
    def __init__(self, api_key: str):
        """
        Initializes the MemeWorthyAnalyzer with an OpenAI API key.
        :param api_key: OpenAI API key for GPT-4o-mini.
        """
        self.client = openai.Client(api_key=api_key)

    def analyze_file(self, file_path: str) -> dict[str, Any]:
        """
        Analyzes the content of a file to determine if it's meme-worthy or suitable for a pump.fun token.
        :param file_path: Path to the file containing post data.
        :return: A structured dictionary containing suggested token launch values and a meme-worthiness score.
        """
        content = self._load_file(file_path)
        prompt = self._construct_prompt(content)
        response = self._query_gpt(prompt)

        return response

    def _load_file(self, file_path: str) -> str:
        """
        Loads content from any text-based file format.
        :param file_path: Path to the file.
        :return: Extracted text content from the file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def _construct_prompt(self, content: str) -> str:
        """
        Constructs a structured prompt for GPT-4o-mini based on the content.
        :param content: Extracted text content.
        :return: A structured string prompt formatted for GPT analysis.
        """
        prompt = (
            "Analyze the following content to determine if it has meme potential or is suitable for launching a pump.fun token.\n\n"
            f"Content:\n{content}\n\n"
            "Respond strictly in valid JSON format with the following fields:\n"
            "{\n"
            '  "meme_worthiness_score": (integer, 1-10),\n'
            '  "name": (string, suggested token name),\n'
            '  "ticker": (string, suggested token ticker),\n'
            '  "description": (string, written in the style of extreme 4chan/reddit shitposting. Make it absurd, degenerate, and hilarious.),\n'
            '  "image_or_video_idea": (string, a meme image or video concept that aligns with viral internet culture),\n'
            '  "telegram_link": (string, optional Telegram community link),\n'
            '  "website_link": (string, optional website link),\n'
            '  "twitter_x_link": (string, optional Twitter/X link)\n'
            "}\n"
            "Ensure the response is a valid JSON string with no extra text before or after the JSON block."
        )
        return prompt

    def _query_gpt(self, prompt: str) -> dict[str, Any]:
        """
        Queries GPT-4o-mini to analyze the prompt and return structured token launch values and a meme-worthiness score.
        :param prompt: The formatted prompt string.
        :return: A structured dictionary with suggested token values and a meme-worthiness score.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in internet culture, viral trends, and crypto token launches. Respond strictly with valid JSON. Do not include any preamble or extra text before or after the JSON response.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )

            response_content = response.choices[0].message.content
            if response_content is not None:
                response_content = response_content.strip()
            else:
                return {"error": "No response content from GPT."}

            return json.loads(response_content)  # Expecting GPT to return valid JSON
        except OpenAIError as e:
            return {"error": f"Failed to process request: {str(e)}"}
        except json.JSONDecodeError:
            return {"error": "GPT response is not a valid JSON format."}


@click.command()
@click.option("--api-key", required=True, help="OpenAI API key.")
@click.option(
    "--file-path",
    required=True,
    type=click.Path(exists=True),
    help="Path to the file containing post data.",
)
def main(api_key: str, file_path: str):
    """Command-line interface for analyzing meme-worthiness and token launch potential."""
    analyzer = MemeWorthyAnalyzer(api_key)
    result = analyzer.analyze_file(file_path)
    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
