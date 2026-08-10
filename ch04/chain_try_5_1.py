from chain_5_1 import web_research_chain

question = 'What can I see and do in the Spanish town of Astorga?'


NUM_SEARCH_QUERIES = 3
NUM_SEARCH_RESULTS_PER_QUERY = 5

web_research_report = web_research_chain.invoke(question)
print(web_research_report)