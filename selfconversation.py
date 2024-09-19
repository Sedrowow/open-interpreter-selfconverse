from interpreter import OpenInterpreter
import sys

topic = str(sys.argv)

if topic is not None:
    print(topic)
else:
   topic = input("what is the topic you want to have to be talked about?\n")


agent_1 = OpenInterpreter()
agent_1.llm.model = "i"
agent_1.system_message = "this is a seperate instance. never create any code!"


agent_2 = OpenInterpreter()
agent_2.llm.model = "i"
agent_2.system_message = "this yet another instance. never create any code!"



def swap_roles(messages):
    for message in messages:
        if message["role"] == "user":
            message["role"] = "assistant"
        elif message["role"] == "assistant":
            message["role"] = "user"
    return messages


agents = [agent_1, agent_2]

# Kick off the conversation
messages = [
    {
        "role": "user",
        "type": "message",
        "content": "Hello, what do you think about the question: can reality be described by words?",
    }
]

while True:
    for agent in agents:
        messages = agent.chat(messages)
        messages = swap_roles(messages)

