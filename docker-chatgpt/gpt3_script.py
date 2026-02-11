import openai

# Add your OpenAI API key
openai.api_key = "..."

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

generated_text = generate_text("Write a short story about a devops trying to understand Kubernetes with humor")
print(generated_text)
