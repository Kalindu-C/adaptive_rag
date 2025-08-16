* .with_structured_output() method - This is the easiest and most reliable way to get structured outputs.
                                   - This method takes a schema as input which specifies the names, types, and descriptions of the desired output attributes.
                                   - The method returns a outputs objects corresponding to the given schema
                                   - The schema can be specified as a TypedDict class, JSON Schema or a Pydantic class.
                                   - If we want the model to return a Pydantic object, we just need to pass in the desired Pydantic class. 
                                   - For more complex schemas it's very useful to add few-shot examples to the prompt. - add examples to a system message
                                           - etc


* retrieval_grader - The retrieval grader acts as a quality control mechanism that evaluates whether retrieved documents are actually relevant to the user’s question. This component is crucial because vector similarity alone doesn’t guarantee relevance — documents might be semantically similar but contextually inappropriate.

This grading step prevents irrelevant documents from contaminating our generation process and triggers web search when local documents are insufficient.

* hallucination_grader - The hallucination grader assesses whether the generated answer is grounded in the provided facts. This is important for ensuring the reliability and accuracy of the information being presented to the user.It compares the generated response against the retrieved documents

* When hallucinations are detected, our system can trigger regeneration or seek additional information, ensuring that users receive accurate and trustworthy responses.

* i got error in this line - answer_grader: RunnableSequence = answer_prompt | structured_llm_grader
The expression answer_prompt | structured_llm_grader creates a RunnableSerializable, but you're trying to assign it to a variable typed as RunnableSequence
