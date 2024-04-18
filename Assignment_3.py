def fifo(pages, frames):
    memory = []  # Initialize the list to keep track of pages in memory
    faults = 0  # Counter for the number of page faults
    fault_steps = []  # List to store detailed step-by-step output
    for page in pages:  # Iterate over each page in the reference string
        if page not in memory:  # Check if the page is not in memory
            if len(memory) < frames:  # Check if there is still space in memory
                memory.append(page)  # Add the new page to memory
            else:
                memory.pop(0)  # Remove the oldest page from memory
                memory.append(page)  # Add the new page to memory
            faults += 1  # Increment the page fault counter
            fault_steps.append(f"Page fault ({page}) - Page Table: {set(memory)}, Frames: {memory.copy()}, Faults: {faults}")
    return fault_steps, faults  # Return the detailed steps and total faults

def lru(pages, frames):
    memory = []  # Initialize the list to keep track of pages in memory
    faults = 0  # Counter for the number of page faults
    fault_steps = []  # List to store detailed step-by-step output
    for page in pages:  # Iterate over each page in the reference string
        if page not in memory:  # Check if the page is not in memory
            if len(memory) < frames:  # Check if there is still space in memory
                memory.append(page)  # Add the new page to memory
            else:
                memory.pop(0)  # Remove the least recently used page from memory
                memory.append(page)  # Add the new page to memory
            faults += 1  # Increment the page fault counter
        else:
            memory.remove(page)  # Remove the page from its current position
            memory.append(page)  # Re-add the page to the end to mark it as recently used
        fault_steps.append(f"Page fault ({page}) - Page Table: {set(memory)}, Frames: {memory.copy()}, Faults: {faults}")
    return fault_steps, faults  # Return the detailed steps and total faults

def optimal(pages, frames):
    memory = []  # Initialize the list to keep track of pages in memory
    faults = 0  # Counter for the number of page faults
    fault_steps = []  # List to store detailed step-by-step output
    for i in range(len(pages)):  # Iterate over each page in the reference string using its index
        page = pages[i]  # Current page in the reference string
        if page not in memory:  # Check if the page is not in memory
            if len(memory) < frames:  # Check if there is still space in memory
                memory.append(page)  # Add the new page to memory
            else:
                # Find the page in memory that will not be used for the longest time
                future = {k: pages[i+1:].index(k) if k in pages[i+1:] else float('inf') for k in memory}
                to_remove = max(future, key=future.get)  # Select the page that has the most distant next use
                memory.remove(to_remove)  # Remove the selected page from memory
                memory.append(page)  # Add the new page to memory
            faults += 1  # Increment the page fault counter
        fault_steps.append(f"Page fault ({page}) - Page Table: {set(memory)}, Frames: {memory.copy()}, Faults: {faults}")
    return fault_steps, faults  # Return the detailed steps and total faults

def simulate_page_replacement(pages, frames):
    algorithms = {'LRU': lru, 'Optimal': optimal, 'FIFO': fifo}  # Dictionary mapping algorithm names to functions
    for name, func in algorithms.items():  # Iterate over each algorithm
        print(f"For {name} Algorithm:")  # Print the algorithm name
        fault_steps, total_faults = func(pages, frames)  # Execute the page replacement algorithm
        for step in fault_steps:  # Print each step of the simulation
            print(f"• {step}")
        print(f"• Total Page Faults: {total_faults}\n")  # Print the total number of page faults

# Input
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 4


# Simulate the page replacement
simulate_page_replacement(pages, frames)

