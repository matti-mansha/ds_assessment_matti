from flask import Flask, request
import openai
import re

app = Flask(__name__)

@app.route('/get-recommended-fruits', methods=['POST'])
def get_recommended_fruits():
    weekend_party = request.form.get('q1_answer')
    flavour = request.form.get('q2_answer')
    texture = request.form.get('q3_answer')
    price_range = request.form.get('q4_answer')
    
    openai.api_key = "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"
    
    prompt = """
    We have 5 ingredient:
    oranges
    apples
    pears
    grapes
    watermelon
    lemon
    lime



    If they party on weekends, apples, pears, grapes, watermelon are allowed.
    If they like cider, show apples, oranges, lemon, lime.
    If they like sweet, show watermelon, orange.
    If they like waterlike, show watermelon.
    If grapes is chosen, remove watermelon from the list.
    If texture you don't like is smooth, remove pears.
    If texture you don't like is slimy, remove watermelon, lime and grape.
    If texture you don't like is waterlike, remove watermelon.
    If price < $3 remove lime, watermelon.
    If price > $4 and < $7 remove pears, apples.

    Recommended fruits: """

    # Add the input answers to the prompt
    prompt += f"\n\nAnswers:\n1. {weekend_party}\n2. {flavour}\n3. {texture}\n4. {price_range}"

    # Generate the text using GPT3 API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n = 1,
        stop=None,
        timeout=10,
    )
    # print(response)

    # Extract the recommendations from the response
    recommendations = re.findall(r'Recommended fruits: (.+)', response.choices[0].text, re.DOTALL)

    return recommendations


