* .with_structured_output() method - This is the easiest and most reliable way to get structured outputs.
                                   - This method takes a schema as input which specifies the names, types, and descriptions of the desired output attributes.
                                   - The method returns a outputs objects corresponding to the given schema
                                   - The schema can be specified as a TypedDict class, JSON Schema or a Pydantic class.
                                   - If we want the model to return a Pydantic object, we just need to pass in the desired Pydantic class. 
                                   - For more complex schemas it's very useful to add few-shot examples to the prompt. - add examples to a system message
                                           - etc