# Universal Data Structures and Algorithms Roadmap

DSA as a supporting skill for a full-stack and AI engineer, not a competitive programming track. Python throughout. Not built around Django, React, VTU, or AI specifically, the knowledge transfers to all of them.

---

## Baseline Audit

**Already covered, review only:** Big-O basics, arrays and strings fundamentals, sorting and searching concepts. Review these quickly inside their phases rather than reteaching from zero.

**Genuinely new:** the explicit problem-solving process, two pointers, sliding window, linked lists, stacks and queues, hash maps in depth, recursion and backtracking, trees/BST, heaps, graphs and graph algorithms, greedy, dynamic programming, pattern recognition across all of it, real-world DSA connections, interview-style problem solving.

**Dependency order:**
- The problem-solving process and Big-O come first, everything else is analyzed through them.
- Two pointers and sliding window build directly on arrays/strings.
- Recursion must come before backtracking, trees, and graph DFS.
- Hash maps are independent and can be learned any time after arrays/strings.
- Stacks and queues are independent, but queues are a prerequisite for BFS.
- Trees depend on recursion.
- Heaps depend on trees at a conceptual level only.
- Graphs depend on recursion, stacks, and queues (DFS and BFS).
- Greedy depends on sorting and basic proof intuition.
- Dynamic programming depends on recursion and is the most demanding topic, placed last.

**Independent, any order once prerequisites are met:** hash maps, stacks, queues.

**Delayed on purpose, not core:** competitive programming, suffix arrays/trees, segment trees, Fenwick trees, advanced graph theory, advanced number theory, randomized algorithms, NP-completeness theory, computational geometry, hundreds of LeetCode grinding. Introduced later only if a specific goal needs them.

**Most important for software engineering:** arrays/strings, hash maps, trees, graphs, sorting/searching, complexity analysis, pattern recognition.

**Primarily interview-oriented, still useful but lower daily-engineering weight:** backtracking, advanced DP, some graph algorithms like Dijkstra and Union-Find.

---

## Phase 1: Problem-Solving Process and Big-O

**Goal:** Install a repeatable process for approaching any problem, and use Big-O as the tool to reason about solutions, not as disconnected math.

**Concepts:**
- Process: understand the problem, inputs/outputs, constraints, examples, edge cases, brute force, identify the bottleneck, optimize, analyze complexity, test
- Big-O: O(1), O(log n), O(n), O(n log n), O(n squared), O(2^n), O(n!)
- Time vs space complexity, best/average/worst case, nested loops, sequential operations, recursion complexity
- Reading complexity directly from code, not from memorized rules

**Prerequisites:** None (review of prior Big-O exposure).

**Practical exercises:** Given five short code snippets, determine time and space complexity from the code itself. Given one unfamiliar problem, write out the full process (understand, examples, constraints, brute force, bottleneck) before writing any code.

**Skills gained:** Can state the complexity of unfamiliar code on sight and can describe a problem-solving plan before coding.

**What NOT to study yet:** Any specific data structure beyond arrays already known.

**Exit criteria:** Given a new snippet with nested loops and a hash lookup, correctly states complexity and explains why in one sentence per term.

---

## Phase 2: Arrays and Strings

**Goal:** Deepen existing array/string knowledge into real patterns used constantly in practice.

**Concepts:**
- Indexing, traversal, insertion, deletion, searching, updating
- Fixed vs dynamic arrays, contiguous memory, random access, operation complexity
- Patterns: counting, frequency tracking, prefix sums, in-place modification, reversing, rotation, partitioning
- Strings as sequences: comparison, substrings, character counting, palindrome checks, mutable vs immutable strings

**Prerequisites:** Phase 1.

**Practical exercises:** Reverse an array in place. Compute a prefix sum array and use it to answer range-sum queries. Check if a string is a palindrome. Find all anagram groups in a list of words.

**Skills gained:** Can implement prefix sums, in-place reversal, and frequency counting without hesitation.

**What NOT to study yet:** Two pointers and sliding window as named patterns, that is next.

**Exit criteria:** Solve a new array/string problem and correctly identify whether prefix sums, frequency counting, or in-place modification fits, before writing code.

---

## Phase 3: Two Pointers

**Goal:** Recognize when two pointers eliminate unnecessary work compared to a brute-force nested loop.

**Concepts:**
- Left/right pointers, fast/slow pointers
- Sorted-array problems, removing duplicates, reversing, partitioning, palindrome checking
- Why two pointers turn O(n squared) into O(n) for the right problem shape

**Prerequisites:** Phase 2.

**Practical exercises:** Remove duplicates from a sorted array in place. Find a pair in a sorted array that sums to a target. Reverse a string using two pointers.

**Skills gained:** Can justify, in one sentence, why two pointers apply to a given problem instead of nested loops.

**What NOT to study yet:** Sliding window is related but distinct, taught next to avoid confusing the two.

**Exit criteria:** Given a new sorted-array problem, correctly decides whether two pointers apply and implements it in under 10 minutes.

---

## Phase 4: Sliding Window

**Goal:** Handle subarray/substring problems efficiently by maintaining a moving window instead of recomputing from scratch.

**Concepts:**
- Fixed-size windows vs variable-size windows
- Expanding and shrinking the window, maintaining window state
- Frequency maps inside a window

**Prerequisites:** Phase 2, 3.

**Practical exercises:** Find the maximum sum of any fixed-size k subarray. Find the longest substring without repeating characters. Find the smallest subarray with a sum at least a target.

**Skills gained:** Can distinguish a sliding-window problem from a two-pointer problem and implement either correctly.

**What NOT to study yet:** Linked lists, unrelated to this pattern.

**Exit criteria:** Given a new substring/subarray problem, correctly identifies fixed vs variable window and implements it without reference.

---

## Phase 5: Linked Lists

**Goal:** Understand linked structures and the operations unique to them, and know when they beat arrays.

**Concepts:**
- Nodes, head, tail, traversal, insertion, deletion
- Singly vs doubly linked lists
- Patterns: reversing a list, fast/slow pointers, finding the middle, cycle detection, merging two sorted lists
- Array vs linked list tradeoff: random access vs insertion/deletion cost

**Prerequisites:** Phase 1 (recursion helps but is not required yet, iterative approach is fine here).

**Practical exercises:** Reverse a singly linked list. Detect a cycle using fast/slow pointers. Find the middle node in one pass. Merge two sorted linked lists.

**Skills gained:** Can implement the four core linked-list patterns without looking them up.

**What NOT to study yet:** Every linked-list variation (skip lists, XOR lists), not useful at this stage.

**Exit criteria:** Can state, for a given problem, whether an array or a linked list is the better fit, with a one-sentence reason.

---

## Phase 6: Stacks and Queues

**Goal:** Understand LIFO and FIFO structures and their real applications.

**Concepts:**
- Stack: push, pop, peek, LIFO, complexity
- Applications: parentheses matching, undo operations, expression evaluation, the call stack itself, monotonic stack introduction
- Queue: enqueue, dequeue, front, FIFO, complexity
- Circular queues, deque concept, the queue's role in BFS, producer/consumer intuition

**Prerequisites:** Phase 1.

**Practical exercises:** Validate matched parentheses using a stack. Implement a queue using two stacks. Solve a basic monotonic-stack problem such as next greater element.

**Skills gained:** Can pick stack vs queue correctly based on whether the newest or oldest item should be processed first.

**What NOT to study yet:** BFS itself, that comes with graphs, this phase only builds the queue skill needed for it.

**Exit criteria:** Solves the next-greater-element problem using a monotonic stack without hints.

---

## Phase 7: Hash Maps

**Goal:** Master hash maps deeply, since they are the single most useful data structure in everyday engineering.

**Concepts:**
- Key/value pairs, hashing, hash functions, collisions, average-case vs worst-case complexity
- Sets vs maps/dictionaries
- Patterns: frequency counting, lookup tables, duplicate detection, grouping, caching, two-sum-style problems
- Why a hash map turns an O(n squared) brute force into O(n)

**Prerequisites:** Phase 1, 2.

**Practical exercises:** Solve two-sum using a hash map in one pass. Group anagrams using a hash map. Find the first non-repeating character in a string.

**Skills gained:** Reflexively reaches for a hash map when a brute-force solution has a nested lookup.

**What NOT to study yet:** Hash map internals like open addressing vs chaining beyond a conceptual level, not needed for engineering work.

**Exit criteria:** Given a brute-force O(n squared) solution, correctly rewrites it as O(n) using a hash map.

---

## Phase 8: Recursion and Backtracking

**Goal:** Understand recursion through the call stack, not as a magic trick, then extend it into backtracking.

**Concepts:**
- Base case, recursive case, the call stack, tracing recursive calls, recursion vs iteration, stack overflow risk
- Backtracking: decision tree, choose, explore, undo, constraints

**Prerequisites:** Phase 1.

**Practical exercises:** Trace a recursive Fibonacci call by hand, drawing the call stack. Implement factorial and Fibonacci recursively. Generate all subsets of a set. Generate all permutations of a list.

**Skills gained:** Can draw a recursive call stack by hand and explain exactly why a given recursive call returns what it returns.

**What NOT to study yet:** Tree and graph recursion specifically, those come once trees and graphs are introduced, this phase covers the recursion mechanics only.

**Exit criteria:** Can trace, on paper, the full call stack of a recursive function with three levels of depth, with no errors.

---

## Phase 9: Sorting and Searching

**Goal:** Deepen existing sorting/searching knowledge, with binary search as the main focus.

**Concepts:**
- Bubble, selection, insertion sort: mechanics and complexity, understood conceptually, not memorized line by line
- Merge sort: divide and conquer, splitting, merging, O(n log n), space tradeoff
- Quick sort: pivot, partitioning, average vs worst case
- Linear search vs binary search
- Binary search in depth: sorted-data requirement, search-space reduction, O(log n), boundary handling, common off-by-one bugs
- Binary search variations: first occurrence, last occurrence, insertion position, binary search on the answer

**Prerequisites:** Phase 1, 2 (review, since already partially studied).

**Practical exercises:** Implement merge sort and quick sort from scratch. Implement binary search and then adapt it to find the first occurrence of a target. Solve one binary-search-on-answer style problem.

**Skills gained:** Can implement binary search correctly on the first attempt, including boundary conditions.

**What NOT to study yet:** Exotic sorts (radix, bucket, heap sort as a named algorithm, that comes naturally once heaps are covered).

**Exit criteria:** Implements binary search from memory with correct boundaries on the first try, no off-by-one errors.

---

## Phase 10: Trees and Binary Search Trees

**Goal:** Understand hierarchical structures and how BST properties enable efficient search.

**Concepts:**
- Tree terminology: root, parent, child, leaf, depth, height, subtree
- Binary trees, traversal: preorder, inorder, postorder, level-order (recursion for the first three, a queue for level-order)
- BST property, search, insertion, deletion, average complexity
- Why an unbalanced BST degenerates into a linked list, balanced trees introduced conceptually only

**Prerequisites:** Phase 6 (queue for level-order), Phase 8 (recursion).

**Practical exercises:** Implement the four traversal orders. Implement BST insertion and search. Given a degenerate insertion order, show how the BST becomes linked-list-like and explain why.

**Skills gained:** Can implement any of the four traversals without hesitation and can explain BST worst-case behavior.

**What NOT to study yet:** AVL trees, Red-Black trees, implementing self-balancing logic, conceptual understanding is enough.

**Exit criteria:** Given an unfamiliar tree problem, correctly picks the traversal order needed and implements it.

---

## Phase 11: Heaps and Priority Queues

**Goal:** Understand how heaps give fast access to the highest or lowest priority item.

**Concepts:**
- Heap concept, min heap, max heap, parent/child relationships
- Insertion, removal, heapify, O(log n) insertion/removal, O(1) access to the top
- Applications: scheduling, top-K problems, priority systems, Dijkstra's algorithm

**Prerequisites:** Phase 10 (conceptual tree shape), Python's heapq module.

**Practical exercises:** Find the k largest elements in a list using a heap. Implement a simple task scheduler that always processes the highest-priority task next.

**Skills gained:** Recognizes top-K and priority-based problems and reaches for a heap instead of sorting the whole input.

**What NOT to study yet:** Manually implementing a heap from scratch beyond understanding heapify once, Python's heapq is used for practical work.

**Exit criteria:** Solves a top-K problem in better than O(n log n) full-sort time, using a heap correctly.

---

## Phase 12: Graphs and Graph Algorithms

**Goal:** Understand graph representation and the two core traversals, then the handful of graph algorithms that are actually useful day to day.

**Concepts:**
- Vertices, edges, directed vs undirected, weighted graphs, adjacency list vs adjacency matrix
- BFS: queue-based, level-by-level, shortest path in unweighted graphs
- DFS: recursion or explicit stack based
- Practice areas: connected components, cycle detection, path finding, grid problems
- Topological sort for dependency ordering
- Dijkstra for shortest paths with nonnegative weights
- Union-Find for connectivity and grouping

**Prerequisites:** Phase 6 (queue), Phase 8 (recursion/stack), Phase 11 (heap, needed for Dijkstra).

**Practical exercises:** Implement BFS and DFS on an adjacency list. Count connected components in a graph. Detect a cycle in a directed graph. Implement topological sort for a small dependency list.

**Skills gained:** Can choose BFS vs DFS correctly based on whether shortest path or full exploration is needed, and can implement both from scratch.

**What NOT to study yet:** Advanced graph theory, network flow, advanced shortest-path variants beyond Dijkstra.

**Exit criteria:** Given a new grid or graph problem, correctly picks BFS or DFS and implements it without reference.

---

## Phase 13: Greedy Algorithms

**Goal:** Recognize when a locally-best choice leads to a globally optimal answer, and know how to check whether greedy is safe.

**Concepts:**
- Greedy intuition: make the best-looking local decision
- When greedy works and when it fails, the need to justify it rather than assume it
- Sorting plus greedy, interval and scheduling problems, activity selection

**Prerequisites:** Phase 9 (sorting).

**Practical exercises:** Solve the activity-selection problem. Solve an interval-merging problem. Given a problem where greedy looks tempting but fails, identify why and find a counterexample.

**Skills gained:** Does not apply greedy blindly, always checks for a counterexample first.

**What NOT to study yet:** Formal greedy-algorithm proof techniques (exchange argument, matroid theory), conceptual justification is enough.

**Exit criteria:** Given a new optimization problem, correctly decides whether greedy is safe or whether DP is needed instead.

---

## Phase 14: Dynamic Programming

**Goal:** Solve problems with overlapping subproblems and optimal substructure systematically, not by pattern-matching to memorized solutions.

**Concepts:**
- Overlapping subproblems, optimal substructure, memoization vs tabulation
- The process: define the state, define the transition, define the base case, determine computation order, analyze complexity
- Progression: Fibonacci and climbing stairs, then grid problems, knapsack concepts, subsequence problems, 2D DP
- Space optimization once a working solution exists

**Prerequisites:** Phase 8 (recursion), Phase 1 (complexity analysis).

**Practical exercises:** Solve climbing stairs with memoization, then tabulation. Solve a grid unique-paths problem. Solve a 0/1 knapsack problem. Solve a longest-common-subsequence problem.

**Skills gained:** Can define state and transition for a new DP problem methodically instead of guessing.

**What NOT to study yet:** Advanced DP on trees or graphs, digit DP, bitmask DP, only needed for later specialization.

**Exit criteria:** Given a new DP problem, correctly writes the state and transition before writing any code, and gets a working tabulated solution.

---

## Phase 15: Patterns and Complexity in Practice

**Goal:** Consolidate everything into pattern recognition and a working complexity intuition, the actual interview and engineering skill.

**Concepts:**
- Full pattern list: frequency counting, two pointers, sliding window, prefix sums, binary search, fast/slow pointers, stack patterns, monotonic stack, BFS, DFS, backtracking, greedy, DP, heap/top-K, intervals, divide and conquer
- The complexity reference table (array index O(1), array search O(n), hash lookup O(1) average, linked-list traversal O(n), stack/queue ops O(1), binary search O(log n), merge sort O(n log n), heap insert/remove O(log n), BFS/DFS O(V+E)), understood by reasoning, not memorized
- Data-structure tradeoffs: array vs linked list, hash map vs array, stack vs queue, heap vs sorted array, tree vs hash map, adjacency list vs matrix

**Prerequisites:** Phases 1 to 14.

**Practical exercises:** Given ten unlabeled problems mixing every pattern above, identify the correct pattern for each before solving any of them. Solve three of the ten fully.

**Skills gained:** Can classify a new, unfamiliar problem into the right pattern family within a minute or two.

**What NOT to study yet:** N/A, this is the integration phase.

**Exit criteria:** Given five new unlabeled problems, correctly identifies the pattern for at least four of them before writing code.

---

## Phase 16: Real-World Connections and Interview Problem Solving

**Goal:** Connect DSA to actual engineering work and practice explaining solutions the way an interview or a code review requires.

**Concepts:**
- Backend connections: caching, request processing, database indexing concepts, queues, task scheduling, rate limiting, lookup tables
- Frontend connections: state management, event queues, rendering work, searching/filtering, memoization
- AI/ML connections: vectors, nearest-neighbor search concepts, graphs, priority queues, search algorithms, DP, complexity of ML operations
- Database connections: indexes, B-tree/B+ tree concepts, hash index concepts, query planning concepts
- Interview process: constraints first, brute force first, optimize, complexity analysis, clean code, edge-case testing
- For a solved problem, being able to state: what it asks, brute force, better approach, data structure used, why it works, time and space complexity, edge cases
- Testing habit for every exercise: normal input, empty input, one element, duplicates, sorted, reverse sorted, large input, boundary cases, invalid input

**Prerequisites:** Phase 15.

**Practical exercises:** Pick five previously solved problems (one per major topic) and write a full explanation of each following the structure above. Solve two new medium-level problems end to end, from constraints to tested working code, explaining the reasoning out loud or in writing at each step.

**Skills gained:** Can explain any solved problem clearly enough for a reviewer or interviewer to follow without gaps, and tests solutions properly instead of assuming correctness from one passing example.

**Exit criteria:** Explains a solved problem's approach, complexity, and edge cases clearly to someone else (or in writing) with no follow-up questions needed.

---

## Final Roadmap Requirements

### Learning Timeline
- Phase 1 to 2 (process, Big-O, arrays/strings): foundation, mostly review
- Phase 3 to 4 (two pointers, sliding window): pattern layer built on arrays
- Phase 5 to 7 (linked lists, stacks/queues, hash maps): core structures
- Phase 8 to 9 (recursion/backtracking, sorting/searching): reasoning and search foundations
- Phase 10 to 12 (trees, heaps, graphs): structural depth
- Phase 13 to 14 (greedy, DP): optimization reasoning, the hardest phases
- Phase 15 to 16: integration, pattern recognition, and interview/real-world application

### Portfolio Checklist
- [ ] A GitHub repo of solved problems, organized by phase/topic, not a random dump
- [ ] At least one problem per phase with a full written explanation (approach, complexity, edge cases)
- [ ] A short write-up connecting one DSA concept to a real project (e.g. caching in the Django roadmap, or a graph structure in an AI project)
- [ ] The Phase 15 pattern-recognition exercise results documented
- [ ] The Phase 16 explanation exercise for five problems documented

### GitHub Project Checklist
- [ ] Clear folder structure by topic (arrays, linked-lists, hash-maps, trees, graphs, dp, and so on)
- [ ] Each solution file includes complexity analysis in a comment or short markdown note
- [ ] README summarizing which patterns are covered and linking to the strongest examples
- [ ] No solutions copied without being rebuilt from memory afterward

### Interview Preparation Checklist
- [ ] Can state complexity of any solution written, without checking
- [ ] Can explain brute force before optimized for any solved problem
- [ ] Can trace a recursive call stack on paper
- [ ] Can implement binary search, BFS, DFS, and a basic DP table from memory
- [ ] Can identify the right pattern for a new problem within two minutes
- [ ] Can list edge cases for a new problem before coding

### Common Interview Questions
- Two-sum, and how a hash map improves it from O(n squared) to O(n)
- Reverse a linked list, iteratively and recursively
- Detect a cycle in a linked list
- Find the k most frequent elements in a list
- Validate matched parentheses
- Level-order traversal of a binary tree
- Number of connected components in a graph
- Longest common subsequence, or a similar classic DP problem
- Merge intervals
- Explain the tradeoff between an array and a linked list for a given use case

### Free Learning Resources
- NeetCode (neetcode.io), pattern-organized problem sets matching this exact structure
- Python official docs for collections.deque and heapq (docs.python.org/3/library/collections.html and docs.python.org/3/library/heapq.html)
- Visualgo (visualgo.net), visual walkthroughs of data structures and algorithms
- MIT OpenCourseWare 6.006 Introduction to Algorithms, for deeper theory on demand, not required reading

### Books (optional deep dives)
- Grokking Algorithms (Aditya Bhargava), simple explanations with visuals, good fit for the WHY-before-HOW preference
- Cracking the Coding Interview (Gayle Laakmann McDowell), for the interview-problem-solving phase specifically

### Practice Websites
- LeetCode, filtered by pattern/tag rather than solved randomly
- NeetCode 150 list, a curated, non-exhaustive problem set matching this roadmap's scope
- HackerRank, for structured topic-based practice sets

### Advanced Topics for After This Roadmap
- Segment trees and Fenwick trees, for range-query-heavy problems
- Advanced graph algorithms: network flow, A*, Bellman-Ford for negative weights
- Advanced DP: bitmask DP, digit DP, DP on trees
- Amortized analysis in more formal depth
- Randomized algorithms, only if a specific project or interview track requires them

---

## Non-Negotiables

- Never skip writing the brute-force solution first, even when the efficient approach is already known.
- Never move to the next phase until the current one's exercises are solved and can be re-explained without notes.
- Always test with the standard edge-case set before considering a solution correct.
- Never memorize a solution instead of understanding the state/transition or the pattern behind it.