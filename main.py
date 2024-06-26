from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

from dbConn import queryDatabase

import re

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

llm = ChatOpenAI(openai_api_key=OPENAI_KEY)
outputParser = StrOutputParser()

systemContext = """ Given the following SQL tables, write queries based on the user's request.
                    Return only the query (ex. SELECT DISTINCT "HouseType" FROM HousingPrices;).
                    The query should be focused on returning raw data without modifying it.
                    For example, if the user asked for a histogram, you should return all the rows instead of using frequency, and let the rest of the program deal with the data.  
                    CREATE TABLE HousingPrices (
                        "HouseType" VARCHAR(255),
                        "Area" VARCHAR(255),
                        "Index" DECIMAL(10, 1),
                        "Benchmark" VARCHAR(255),
                        "Yr./Yr. % Chg." DECIMAL(5, 2)
                    );
                    
                    CREATE TABLE WeatherData (
                        "Month" INT,
                        "Region" VARCHAR(255),
                        "HighTemperature" INT,
                        "LowTemperature" INT,
                        "RainfallMM" DECIMAL,
                        "DaylightHours" DECIMAL
                    );
                """
#inputPrompt = input(">>> ")
inputPrompt = "can i get a scatter plot of the low and high temperatures over time (months) in toronto and vancouver"

prompt = ChatPromptTemplate.from_messages([
    ("system", systemContext),
    ("user", "{input}")
])

sqlQueryChain = prompt | llm | outputParser
query = sqlQueryChain.invoke({"input": inputPrompt})
sqlQueryData = queryDatabase(query)

systemContext = """
                You are to generate python code that will be passed into an exec() function.
                You must also call the function at the end (ex. create_histogram(sqlQueryData).
                THIS IS ABSOLUTELY MANDATORY AND MUST MUST MUST BE INCLUDED.
                The data passed in will be in a variable called 'sqlQueryData'."
                Here is an example for a request for 'a histogram of benchmarks':
                def create_histogram(rows):
                    import matplotlib.pyplot as plt
                    data = [(str(row[0]), row[1]) for row in rows]
                    benchmarks = [row[0] for row in data]
                    frequencies = [row[1] for row in data]
                    plt.bar(benchmarks, frequencies)
                    plt.xlabel('Benchmark')
                    plt.ylabel('Frequency')
                    plt.title('Histogram of Benchmarks')
                    plt.show()
                create_histogram(sqlQueryData)
                """

prompt = ChatPromptTemplate.from_messages([
    ("system", systemContext),
    ("user", "{input}")
])

print(systemContext)

palPrompt = (
    "Given the prompt: " + inputPrompt +
    " with the following SQL statement: " + query +
    " that returned the following data (only a fraction of it is displayed): " + str(sqlQueryData[:min(3, len(sqlQueryData))]) +
    " generate a python function to create a graph fulfilling the request. Only return the python function with no other text."
)
palChain = prompt | llm | outputParser
generatedCode = palChain.invoke({"input": palPrompt})

if "sqlQueryData" not in generatedCode:
    regex = r'def\s+(\w+)\s*\(.*\):'
    functionNames = re.findall(regex, generatedCode)
    functionName = "print"
    if len(functionNames) > 0:
        functionName = functionNames[0]
    generatedCode += "\n\n" + functionName + "(sqlQueryData)"

print(generatedCode)
exec(generatedCode)
