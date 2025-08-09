from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template=""" 
    Tell me about '{player_input}' in terms of '{category_input}'
    """,
    input_variables=['player_input','category_input']
)
template.save('template.json')