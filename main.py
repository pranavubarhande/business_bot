import google.generativeai as genai
import streamlit as st
import os
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Set up the model
generation_config = {
"temperature": 0.9,
"top_p": 1,
"top_k": 1,
"max_output_tokens": 2048,
}

safety_settings = [
{
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
{
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                            generation_config=generation_config,
                            safety_settings=safety_settings)
prompt_parts = [
    "input:Netflix, in a nutshell, is a giant entertainment library you access through the internet. Here's a breakdown of their business:What they do:Netflix is a streaming service, meaning you watch shows and movies online instead of downloading them or getting physical copies.They offer a vast library of content, including:Original shows and movies: Netflix produces its own content, like \"Stranger Things\" or \"The Crown\".Licensed content: They also acquire rights to stream movies and shows from other studios and production companies.Their service is available in over 190 countries and offers content in multiple languages.How they make money:Netflix operates on a subscription model. Users pay a monthly fee to access the entire library of content.They offer different subscription tiers, often with varying streaming quality or the number of screens you can watch on simultaneously.Some interesting facts:Netflix started in 1997 as a DVD-by-mail service, but they pivoted to streaming in 2007.As of January 2024, they boast over 260 million paid memberships worldwide, making them the leading streaming service.They are constantly investing in creating high-quality original content to stay ahead of the competition. Based on above knowledge answer my following questions. These questions will be asked by someone else so answer in that grammar  way. How do you make money?",
    "output:Netflix operates on a subscription-based business model. Users pay a monthly fee to access the company's vast library of movies, TV shows, and other content. Netflix offers different subscription tiers, with varying levels of streaming quality and the number of screens that can be used simultaneously.",
    "input:Netflix, in a nutshell, is a giant entertainment library you access through the internet. Here's a breakdown of their business:What they do:Netflix is a streaming service, meaning you watch shows and movies online instead of downloading them or getting physical copies.They offer a vast library of content, including:Original shows and movies: Netflix produces its own content, like \"Stranger Things\" or \"The Crown\".Licensed content: They also acquire rights to stream movies and shows from other studios and production companies.Their service is available in over 190 countries and offers content in multiple languages.How they make money:Netflix operates on a subscription model. Users pay a monthly fee to access the entire library of content.They offer different subscription tiers, often with varying streaming quality or the number of screens you can watch on simultaneously.Some interesting facts:Netflix started in 1997 as a DVD-by-mail service, but they pivoted to streaming in 2007.As of January 2024, they boast over 260 million paid memberships worldwide, making them the leading streaming service.They are constantly investing in creating high-quality original content to stay ahead of the competition. Based on above knowledge answer my following questions. These questions will be asked by someone else so answer in that grammar  way. what do you offer?",
    "output: Netflix offers a vast library of content, including both original shows and movies, as well as licensed content from other studios and production companies. The content library includes a wide variety of genres, including action, adventure, comedy, drama, horror, science fiction, and more. Netflix also offers a variety of children's programming.",
    ]
def process_input(input_text):
    prompt_parts.append(input_text)
    response = model.generate_content(prompt_parts)
    print(response.text)
    return f"{response.text}"
    
def main():
    st.title("Netflix Business Bot")

    # Get user input
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        # Process user input and generate response
        response = process_input(user_input)
        # st.text_area("Bot:", value=response, height=500)
        formatted_response = f"**Bot:** {response}"
        st.markdown(formatted_response)

if __name__ == "__main__":
    main()