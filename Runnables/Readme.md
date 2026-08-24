Runnables :
Two type of Runnables:
1. Task Specific Runnable
2. Runnables Premitives

1.Task Specific Runnables:
            • Definition: These are core LangChain components that have been converted into Runnables so they can be used in pipelines.
            • Purpose: Perform task-specific operations like LLM calls, prompting, retrieval, etc.
            • Examples:
            • ChatOpenAI → Runs an LLM model.
            • PromptTemplate → Formats prompts dynamically.
            • Retriever → Retrieves relevant documents.

2. Runnbales Prermitives:
            • Definition: These are fundamental building blocks for structuring execution logic in AI workflows.
            Purpose: They help orchestrate execution by defining how different Runnables interact (sequentially, in parallel, conditionally, etc.).
            • Examples:
                RunnableSequence → Runs steps in order (| operator).
                RunnableParallel → Runs multiple steps simultaneously.
                RunnableMap → Maps the same input across multiple functions.
                RunnableBranch → Implements conditional execution (if-else logic).
                RunnableLambda → Wraps custom Python functions into Runnables.
                RunnablePassthrough → Just forwards input as output (acts as a placeholder).



