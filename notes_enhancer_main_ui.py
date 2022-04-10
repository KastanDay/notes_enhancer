import requests
import json
from tkinter import *
import openai

window = Tk()

# Window Config
window.title('Notes Enhancer')
window.geometry('500x50')

openai.api_key = None # <<PASTE_YOUR_API_KEY_HERE>>

def get_country_info(**search_query):

    search_query = txt.get()
    
    # check input
    print(search_query)
    if len(search_query) == 0:
        print("💥 💥 MUST ENTER QUERY")
        return -1

    # popup window
    root = Tk()
    root.geometry('1000x1200')
    root.title("Search: " + search_query)
    # frame
    frame=Frame(root, width=950, height=1150)
    frame.pack()
    # textbox
    text = Text(frame)
    text.place(x=10, y=10, height=1150, width=1150)
    
    
    
    # demo tester response
    # response = json.load(open("one_search_response.json"))
    response = openai.Engine("ada").search(
        search_model="ada", 
        query=search_query, 
        max_rerank=5,
        file="file-NdM8EkdPCKFmEcL9ksaKR27K",
        return_metadata=True
    )
    
    # iterate through results
    for document in response['data']:
        text.insert(END, 'Title: {}\n{}\n\n---------------------------\n\n'.format(document['metadata']['title'], document['text']))

# Create Label
lbl = Label(window, text='Search query:')
lbl.grid(column=0, row=0, sticky=E)

# Create Entry Field
txt = Entry(window, width=30)
txt.grid(column=1, row=0, sticky=W)

# Create Button
btn = Button(window, text='Go', command=get_country_info)
btn.grid(column=2,row=0, sticky=W)

# btn.pack()
# btn.insert(END)


window.mainloop()
