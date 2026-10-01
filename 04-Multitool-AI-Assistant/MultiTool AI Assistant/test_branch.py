"""
Test for the stateful conditional LCEL workflow.

Demonstrates:
- RunnablePassthrough
- RunnablePassthrough.assign()
- State enrichment
- RunnableBranch conditional routing
"""

from chains.branch_chain import (
    stateful_workflow,
    branch_chain,
)


# ==========================================================
# TEST 1 - GREETING ROUTE
# ==========================================================

question = "hello"

state = stateful_workflow.invoke(question)

print("=" * 70)
print("TEST 1 - GREETING ROUTE")
print("=" * 70)

print("\nQuestion:")
print(state["question"])

print("\nWorkflow State:")
print(state)

print("\nSelected Route:")
print(state["category"])

print("\nFinal Result:")
print(branch_chain.invoke(question))


# ==========================================================
# TEST 2 - GENERAL ROUTE
# ==========================================================

question = "Explain artificial intelligence"

state = stateful_workflow.invoke(question)

print("\n" + "=" * 70)
print("TEST 2 - GENERAL ROUTE")
print("=" * 70)

print("\nQuestion:")
print(state["question"])

print("\nWorkflow State:")
print(state)

print("\nSelected Route:")
print(state["category"])

print("\nFinal Result:")

try:
    print(branch_chain.invoke(question))

except Exception as e:
    print("LLM route unavailable:")
    print(e)