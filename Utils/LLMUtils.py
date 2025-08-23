from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def generic_prompt(prompt):

    response = client.completions.create(
        # model="deepseek-ai.deepseek-r1-distill-qwen-7b",  # You can use any appropriate model
        model = "meta-llama-3.1-8b-instruct",
        prompt=prompt,
        # max_tokens=50 # Smaller tokens return quicker but lack a long explanation
    )

    return response