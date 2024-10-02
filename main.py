import os
from embedchain import App
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")



app = App()
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
result = app.query("What is the net worth of Elon Musk today?")
print(result)