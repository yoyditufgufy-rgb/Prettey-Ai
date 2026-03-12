import json
import os
print("---------------------------AI-----------------------")
#desktop per file ka rasta
file_path = os.path.join(os.path.expanduser("~"), "Desktop", "Ai_memory.json")
# memmory ko load krega
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        memory = json.load(f)
else:
    memory = {}
print("Ai ready btao kya kerna hai.")
while True:
    #check kerga ki answer hai ya nhi
    user_input = input("Bolo: ").lower()
    
    if user_input == "exit":
        print("By boss kal milenge.")
        break
    elif user_input in memory:
        print("Ai: " + memory[user_input])

    else:
        print("Ai: Boss, Mujhe iske bare me nhi pata hai, btao kya answer hai iska. ya fir rhene do. ")
        new_answer = input("Btao: ")
#answer ko memory me save kerne ke liye
        if new_answer.lower() == "rhene do":
            print("Ok ise skip ker dete hai.")
            continue
        else:
            memory[user_input] = new_answer
            with open(file_path, "w" ) as f:
                json.dump(memory, f, indent=4)
            print("Ai: Shabaash maine sikh liya.")
