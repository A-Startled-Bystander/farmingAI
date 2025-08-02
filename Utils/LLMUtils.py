from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def generic_prompt(prompt):

    response = client.completions.create(
        model="deepseek-ai.deepseek-r1-distill-qwen-7b",  # You can use any appropriate model
        prompt=prompt,
        # max_tokens=50
    )

    return response