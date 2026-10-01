from chains.passthrough_chain import passthrough_chain


response = passthrough_chain.invoke(
    "Explain Machine Learning in simple words."
)

print("\nRESULT:\n")
print(response)