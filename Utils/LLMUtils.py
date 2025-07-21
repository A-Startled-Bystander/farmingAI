from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def identify_table_of_contents(pages):
    ret_obj = []
    for page in pages:
        content = page['page_content']
        headers_found_format = "List Of Content Headers Discovered: 1. Header 1; 2. Header 2; 3. Header 3"
        prompt = (
            "Classify the following document text.\n"
            "If it looks like a table of contents, respond with 'Yes'.\n"
            "If it does not, respond with 'No'.\n"
            "Respond with a single word only: Yes or No. Do not provide any explanation.\n\n"
            f"Text:\n{content}\n\n"
            "Answer (Yes or No):"
        )

        print(f"Generating LLM response for page {page["page_num"]}")
        response = client.completions.create(
            model="deepseek-ai.deepseek-r1-distill-qwen-7b",  # You can use any appropriate model
            prompt=prompt,
            # max_tokens=50
        )



        ret_obj.append({
            "page_content": content,
            "prompt": prompt,
            "response": response.choices[0].text
        })

    print()
    return None