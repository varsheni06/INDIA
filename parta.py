def calculate_probabilities(die_values):
    sums = [a + b for a in die_values[0] for b in die_values[1]]
    probabilities = {val: sums.count(val) / len(sums) for val in set(sums)}
    return probabilities

def update_die_values(die, index, value):
    die[index] += value

def dicedooming(A, B):
    original_probabilities = calculate_probabilities([A, B])
    newA = [1, 4, 0, 0, 0, 0]
    newB = [1, 8, 0, 0, 0, 0]

    for i in range(5):
        update_die_values(newA, i + 2, 1)
        
        for x in range(2, 8):
            for y in range(2, 8):
                if x == y:
                    continue

                D = [2, 3, 4, 5, 6, 7]
                D.remove(x)
                D.remove(y)

                print(D, end=" ")
                update_die_values(newB, 2, D[0])
                update_die_values(newB, 3, D[1])
                update_die_values(newB, 4, D[2])
                update_die_values(newB, 5, D[3])

                new_probabilities = calculate_probabilities([newA, newB])

                if new_probabilities == original_probabilities:
                    return newA, newB

    return [], []

def get_user_input():
    values = []
    print("Enter initial face values for Die A and Die B:")
    for _ in range(6):
        values.append(int(input()))
    return values

def main():
    A = get_user_input()
    B = A.copy()

    print("Die A:", A)
    print("Die B:", B)
    
    newA, newB = dicedooming(A, B)

    print("\nNew Die A:", newA)
    print("New Die B:", newB)

if __name__ == "__main__":
    main()
