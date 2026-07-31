from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict , Annotated,Literal,Optional

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

# schema
class Review(TypedDict):

    key_themes : Annotated[list[str],"Write down all the key themes discussed in the review"]
    summary: Annotated[str,"Give a breif review"]
    sentiment: Annotated[Literal["pos","neg"],"GIve the sentiment either negative,positive or neutral"]
    pros : Annotated[Optional[list[str]],"return the pros if availaible"]
    cons : Annotated[Optional[list[str]],"Return the cons if availaible"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke(""""I recently upgraded to the Samsung Galaxy S24 Ultra, 
                                and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor 
                                makes everything lightning fast-whether I'm gaming, multitasking, or editing photos.
                                The 5000mAh battery easily lasts a full day even with heavy use,
                                and the 45W fast charging is a lifesaver.
                                The S-Pen integration is a great touch for note-taking and quick sketches, 
                                though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning,
                                capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
                                However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides?
                                The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors.""")

print(result)



# NOTE : when we invoke with_structered_output then in back a instruction is invoked to the model which is like this
# You are an ai assitant and extract summary,sentiment in json format.
# "Annotated" is used to tell the model what to do in case model fails to understand by one word.
# "optional" as the name suggest.it's used to tell model something is optional not mandatory to provide.if its availiable then provide else leave.
# "literal" it is used to give options according to the user.

# NOTE : This is llm which has already built in json format system which is being provoked by 
# with_structured_output().