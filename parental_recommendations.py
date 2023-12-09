"""
Copyright (C) 2023 Logan Dhillon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Use report card to get recommendations on what to do from GPT-4

import openai

with open("secret_openai-api-key", "r") as f:
    openai.api_key = f.read()

def prompt_gpt(prompt: str) -> str:
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI designed to give students and parents recommendations on their school life based on the information they provide you."},
            {"role": "user", "content": prompt}
        ]
    )['choices'][0]['message']['content']

def prompt_report_card(grade, school, report_card):
    return prompt_gpt(f"""Grade: {grade}, School: {school}
                 
                 Report Card:
                 {report_card}""")

print(prompt_report_card("10", "Halton District School Board", "Math: B, English: A-, Science: C+"))