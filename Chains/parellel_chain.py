from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt1 = PromptTemplate(
    template="Give short and simple notes from the following {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 short questions answers from the following {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template=""" Merge the provided notes and quiz into a single document \n 
            Do NOT use Markdown.
            Do NOT use **bold**.
            Return plain text only.

            notes: {notes} and quiz:{quiz}""",
    input_variables= ["notes","quiz"]
)

parser = StrOutputParser()

parellel_chain = RunnableParallel({
    "notes": prompt1 | model | parser,
    "quiz": prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

final_Chain = parellel_chain | merge_chain

text = '''
    Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
'''

result = final_Chain.invoke({"text":text})

print(result)