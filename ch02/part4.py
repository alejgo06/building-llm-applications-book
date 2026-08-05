from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",  # opcional si es el default
    temperature=0.7,
)

examples = [
  {
      "number": 6,
      "reasoning": "not divisible by 5 nor by 7",
      "result": "None"
  },
  {
      "number": 15,
      "reasoning": "divisible by 5 but not by 7",
      "result": "Abra"
  },
  {
      "number": 12,
      "reasoning": "not divisible by 5 nor by 7",
      "result": "None"
  },
  {
      "number": 21,
      "reasoning": "divisible by 7 but not by 5",
      "result": "Kadabra"
  },
  {
      "number": 70,
      "reasoning": "divisible by 5 and by 7",
      "result": "Abra Kadabra"
  } ]

example_prompt = PromptTemplate(input_variables=["number", "reasoning", "result"], template="{number} \\ {reasoning} \\ {result}")
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Classify the following numbers as Abra, Kadabra or Abra Kadabra: {comma_delimited_input_numbers}",
    input_variables=["comma_delimited_input_numbers"]
)

prompt_input = few_shot_prompt.format(comma_delimited_input_numbers="3, 4, 5, 7, 8, 10, 11, 13, 35.")

response = llm.invoke(prompt_input)
print(response.content)