# Numpy is imported; seed is set
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
# Initialize all_walks
all_walks = []

# # Simulate random walk 10 times
# for i in range(10) :

#     # Code from before
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)

#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)
#         random_walk.append(step)

#     # Append random_walk to all_walks
#     all_walks.append(random_walk)

# # Convert all_walks to Numpy array: np_aw
# np_aw=np.array(all_walks)

# # Plot np_aw and show
# plt.plot(np_aw)
# plt.show()

# # Clear the figure
# plt.clf()

# # Transpose np_aw: np_aw_t
# np_aw_t=np.transpose(np_aw)

# # Plot np_aw_t and show
# plt.plot(np_aw_t)
# plt.show()


# # Simulate random walk 250 times
# for i in range(250) :

#     # Code from before
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)

#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)


#         # Implement clumsiness
#         if np.random.rand()<=0.001 :
#             step = 0

#         random_walk.append(step)

#     # Append random_walk to all_walks
#     all_walks.append(random_walk)

# # Create and plot np_aw_t
# np_aw_t = np.transpose(np.array(all_walks))
# plt.plot(np_aw_t)
# plt.show()

# Simulate random walk 500 times
for i in range(500) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)


        # Implement clumsiness
        if np.random.rand()<=0.001 :
            step = 0

        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends=np_aw_t[-1]
print(ends)

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

count=ends>60
sim=len(ends[count])/500
print(sim)