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
from flask import Flask

app = Flask(__name__)

class Grade:
    def __init__(self, name, code, grade) -> None:
        self.name = name
        self.code = code
        self.grade = grade

    def __str__(self) -> str:
        return f"{self.name} ({self.code}): {self.grade}%"

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

def prompt_report_card(grade, school, grades):
    report_card = ""
    for grade in grades:
        report_card += str(grade) + '\n'

    return prompt_gpt(f"""Grade: {grade}, School: {school}
                 
                 Report Card:
                 {report_card}""")

@app.route("/get_code")
def get_name_from_code(code: str) -> str:
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI designed to get the full name of a course based on it's course code. For example, MPM2D1 would be Principles of Mathematics. Just send the course name, do not explain."},
            {"role": "user", "content": f"What is the course name of {code}"}
        ]
    )['choices'][0]['message']['content']

print("EduSpark is getting your tips ready...")






# EduSpark helps you with your school life using intelligent AI to analyze
# your academics. This can include your report card, as shown below.



print(prompt_report_card("10", "Halton District School Board", [
                         Grade("Math", "MPM2D1", "98.2"),
                         Grade("English", "ENG2D1", "79.3"),
                         Grade("Science", "SNC2O1", "87.8"),
                         Grade("History", "HTY2W1", "69.1")]))
















# if __name__ == "__main__": app.run()