from utilities import to_obj
from chain_2_1 import web_searches_chain
from chain_1_2 import assistant_instructions_chain
from chain_3_1 import search_result_urls_chain

question = 'What can I see and do in the Spanish town of Astorga?'

assistant_instruction_dict = assistant_instructions_chain.invoke(question)
assistant_instruction_dict['user_question']=question

web_searches_list = web_searches_chain.invoke(assistant_instruction_dict)

print(web_searches_list[0])


web_search_dict = web_searches_list[0]
result_urls_list = search_result_urls_chain.invoke(web_search_dict)
print(result_urls_list)

