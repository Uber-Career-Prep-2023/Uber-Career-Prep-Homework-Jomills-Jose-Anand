# Question 9: Adopt a Pet

# * Approach followed: queue
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input stream of pets/people
# * Output: print the pet to be adopted

# * Time taken: 14 minutes


# ? Function to determine the pet to be adopted
def petToAdopt(petType, petQueue):
    for pet in petQueue:
        if pet[1] == petType:
            petQueue.remove(pet)
            return pet
    return petQueue.pop(0)


# ? Function to adopt a pet
def adoptAPet():

    # Initialize the queue
    petQueue = []

    # Iterate over the input stream
    while True:
        # Get the input
        stream = eval(input())

        # If the input is empty, break
        if not stream:
            break

        # If the input is a person, adopt the pet
        if (stream[1] == "person"):
            print(petToAdopt(stream[2], petQueue))

        # If the input is a pet, add it to the queue
        else:
            petQueue.append(stream[:2])


# ? Test cases

# Test case 1
adoptAPet() # All inputs with quotes
"""
Sadie, dog, 4 days
Woof, cat, 7 days
Chirpy, dog, 2 days
Lola, dog, 1 days

Input: Bob, person, dog
Output: Sadie, dog

Input: Floofy, cat
Output:

Input: Sally, person, cat
Output: Woof, cat

Input: Ji, person, cat
Output: Floofy, cat

Input: Ali, person, cat
Output: Chirpy, dog
"""