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
    "input:CARS24, founded in 2015, is a leading AutoTech company streamlining and revolutionizing the sale, purchase, and financing of pre-owned cars in India, Australia, Thailand, and UAE. Leveraging a Smart AI Pricing Engine and 140 quality checks, selling and buying pre-owned vehicles is seamless and transparent with CARS24. Ensuring complete transparency and faster lending processes, CARS24 Financial Services Private Limited, a professionally managed Non-Banking Financial Company (NBFC) registered with the Reserve Bank of India, offers customers focused value-added services. CARS24 promises to be the first-class destination for second-hand cars, simplifying the daunting process of finding, negotiating, examining, and purchasing pre-owned cars in a scattered market. By bringing together cutting-edge technology and country-wide partners, CARS24 solves all problems associated with selling an existing car or purchasing a pre-loved one. Their dedicated in-house researchers work to understand customers' desires and create delightful buying or selling experiences. When you buy a car from CARS24, you get cars ready for the road, each undergoing 140 quality checks and refurbished at state-of-the-art Mega Refurbishment Labs (MRL). They offer a 7-day return policy and flexible finance options with zero down payment and up to a 6-year loan tenure at the lowest interest rates. When you sell on CARS24, you get a great price facilitated by the largest dealer network and Smart AI Pricing Engine, along with instant payment and hassle-free documentation. CARS24 provides seller protection policy, offering legal support in case of accidents or speeding tickets incurred by the new owner. With CARS24 Financial Services, customers get simpler, safer, faster, and more accessible financial services, including loan approval in seconds, same-day disbursal, low-interest rates, and a 100% digitized process ensuring complete transparency.What's Cars24 in nutshell?",
    "In a nutshell, CARS24 is a pioneering AutoTech company founded in 2015. It has redefined the pre-owned car market in India, Australia, Thailand, and UAE by offering streamlined processes for selling, purchasing, and financing vehicles. Utilizing advanced technology like a Smart AI Pricing Engine and conducting 140 quality checks, CARS24 ensures seamless and transparent transactions. Additionally, its financial arm, CARS24 Financial Services Private Limited, provides focused value-added services, including simplified lending processes. The company's mission is to be the top destination for second-hand cars, offering a hassle-free experience for both buyers and sellers through cutting-edge technology and a wide network of partners. With a commitment to transparency, CARS24 guarantees quality cars ready for the road, flexible finance options, and instant payments for sellers. Moreover, it offers comprehensive seller protection policies and customer-focused financial services, making the entire process simpler, safer, and faster."
    "input:CARS24, founded in 2015, is a leading AutoTech company streamlining and revolutionizing the sale, purchase, and financing of pre-owned cars in India, Australia, Thailand, and UAE. Leveraging a Smart AI Pricing Engine and 140 quality checks, selling and buying pre-owned vehicles is seamless and transparent with CARS24. Ensuring complete transparency and faster lending processes, CARS24 Financial Services Private Limited, a professionally managed Non-Banking Financial Company (NBFC) registered with the Reserve Bank of India, offers customers focused value-added services. CARS24 promises to be the first-class destination for second-hand cars, simplifying the daunting process of finding, negotiating, examining, and purchasing pre-owned cars in a scattered market. By bringing together cutting-edge technology and country-wide partners, CARS24 solves all problems associated with selling an existing car or purchasing a pre-loved one. Their dedicated in-house researchers work to understand customers' desires and create delightful buying or selling experiences. When you buy a car from CARS24, you get cars ready for the road, each undergoing 140 quality checks and refurbished at state-of-the-art Mega Refurbishment Labs (MRL). They offer a 7-day return policy and flexible finance options with zero down payment and up to a 6-year loan tenure at the lowest interest rates. When you sell on CARS24, you get a great price facilitated by the largest dealer network and Smart AI Pricing Engine, along with instant payment and hassle-free documentation. CARS24 provides seller protection policy, offering legal support in case of accidents or speeding tickets incurred by the new owner. With CARS24 Financial Services, customers get simpler, safer, faster, and more accessible financial services, including loan approval in seconds, same-day disbursal, low-interest rates, and a 100% digitized process ensuring complete transparency. What do you offer?",
    "output: CARS24 offers streamlined processes for buying, selling, and financing pre-owned cars, leveraging advanced technology, a wide network, and comprehensive services to ensure seamless and transparent transactions.",
    ]
def process_input(input_text):
    prompt_parts.append(input_text)
    response = model.generate_content(prompt_parts)
    print(response.text)
    return f"{response.text}"
    
def main():
    st.title("Cars24 Business Bot")

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