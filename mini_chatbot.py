from ollama import chat
system_msg="You are allu arjun. Answer in movie dialouge. Answer in one sentence adn only in telugu"
print("welcome to allu arjun chatbotpython...........🙄🙄🙄🙄")
history=[]
question_counter=0
while True: 
    question =input("you:")
    if question=="":
        print("allu arjun🤖: please type something😠😠😠😠")
    if question.lower().strip()=="/history":
        print("_________your Converstion so far_______")
        if len(history)<2:
            print("nothing here so far___________")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="you"
            else:
                speaker="allu arjun🤖"
            print(f"{speaker}:{msg["content"]}")
        print("_______________________________________")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("your history is cleared. start a fresh conversation.")
        continue
    if question.lower().strip()=="/help":
        print("___available commands___")
        print("/history - dislpays conversation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbots")
        print("_____________________________________-")
        print()
        continue
    if question.lower().strip()=="exit":
        print("allu arjun🤖: Goodbye user. please come back soon!😠😠😠😠")
        break

    history.append({"role":"user","content":question})
    question_counter+=1
    try:
        response=chat(
                model="llama3.2",
                messages=history
            )
        reply=response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"allu arjun🤖:{reply}")
        print()
        print("-------------------------------------------------")
    except Exception as e:
        print("Unknown issue.Is Ollama running?")