from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

from dbConn import queryDatabase



load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

llm = ChatOpenAI(openai_api_key=OPENAI_KEY)
outputParser = StrOutputParser()

inputPrompt = input(">>> ")
systemContext = """ Given the following SQL tables, write queries based on the user's request.
                    Return only the query (ex. SELECT DISTINCT "HouseType" FROM HousingPrices;).
                    CREATE TABLE HousingPrices (
                        "HouseType" VARCHAR(255),
                        "Area" VARCHAR(255),
                        "Index" DECIMAL(10, 1),
                        "Benchmark" VARCHAR(255),
                        "Yr./Yr. % Chg." DECIMAL(5, 2)
                    );
                """


prompt = ChatPromptTemplate.from_messages([
    ("system", systemContext),
    ("user", "{input}")
])

chain = prompt | llm | outputParser | queryDatabase
response = chain.invoke({"input": inputPrompt})
