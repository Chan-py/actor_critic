import pickle 
import matplotlib.pyplot as plt

with open('losses.pkl', 'rb') as f:
    rewards_all = pickle.load(f)

reward = []
L = 0
rewards_all = rewards_all[1]
for index in range(len(rewards_all)):
    if index == 0:
        continue

    L += rewards_all[index]
    if index % 10 == 0:
        reward.append(L/10)
        L = 0
    
plt.close()
plt.plot(reward)
plt.savefig("train_reward.png")