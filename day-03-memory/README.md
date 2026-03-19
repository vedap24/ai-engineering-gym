# Day 3: Stateful Agent & Queue DSA 🧠

## 🤖 1. AI Memory Agent (`chat_agent.py`)
Built a conversational agent that remembers past interactions using a `while` loop and a `List` of `Dictionaries`. Implemented a sliding window memory (Queue logic) to prevent token limit errors by removing the oldest messages.

## ⚡ 2. DSA Optimization (`recent_counter.py`)
Solved LeetCode 933 (Number of Recent Calls) using Python's `collections.deque`. Optimized the time complexity to $O(1)$ using the `popleft()` method and logical `and` operators to efficiently manage a 3000ms moving window.