import numpy as np
import gym
import math
import pickle as pkl

env = gym.make('CartPole-v0')

#@Q3_tips
def q_index(observation, num_buckets):
    total_index = np.prod(num_buckets)
    x, x_dot, theta, theta_dot = observation
    index = 0

    x_thr = env.env.x_threshold + 1
    x_dot_thr = 100
    theta_thr = math.radians(15)
    theta_dot_thr = math.radians(50)

    x_bins = np.linspace(-x_thr, x_thr, num=num_buckets[0] + 1)
    index += (np.digitize(x, x_bins) - 1) * total_index / num_buckets[0]

    x_dot_bins = np.linspace(-x_dot_thr, x_dot_thr, num=num_buckets[1] + 1)
    index += (np.digitize(x_dot, x_dot_bins) - 1) * total_index / num_buckets[1] / num_buckets[0]

    theta_bins = np.linspace(-theta_thr, theta_thr, num=num_buckets[2] + 1)
    index += (np.digitize(theta, theta_bins) - 1) * total_index / num_buckets[2] / num_buckets[1] / num_buckets[0]

    theta_dot_bins = np.linspace(-theta_dot_thr, theta_dot_thr, num=num_buckets[3] + 1)
    index += (np.digitize(theta_dot, theta_dot_bins) - 1) * total_index / num_buckets[3] / num_buckets[2] / num_buckets[
        1] / num_buckets[0]
    index = total_index-1 if index >= total_index else index

    return np.int(index)



gamma = 0
epsilon = 1.0
epsilon_decay = 0.998
epsilon_min = 0.1
alpha = 0.1
episode = []
max_score = 0;
scores = []

num_buckets = np.array([1, 1, 8, 4])  # x, x_dot, theta, theta_dot
q_table = np.zeros((np.prod(num_buckets), env.action_space.n))
env._max_episode_steps = 1000
episodes = 30
for i in range(episodes + 1):
    observation = env.reset()
    gamma += 0.1
    score = 0
    for _ in range(1000):
        st = q_index(observation, num_buckets)
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[st])
        epsilon *= epsilon_decay
        observation, reward, done, info = env.step(action)
        score += reward
        if abs(observation[0]) > 2.4 or abs(observation[2]) > math.radians(15):
            break
        st_new = q_index(observation, num_buckets)
        q_table[st, action] = (1 - alpha) * q_table[st, action] + alpha * (
                reward + gamma * np.amax(q_table[st_new]))
        if done:
            break

    scores.append(score)
    episode.append((q_table, gamma, score))
    if max_score < score:
        max_score = score
        max_episode = (q_table, gamma, score)
        print(i)

print(scores)
print(max(scores))
print("max")
print(max_episode)

env.close()


answers = {'Q3_i': episode, 'Q3_ii': max_episode}
f = open('Q3.pkl', 'wb')
pkl.dump(answers, f)
f.close()