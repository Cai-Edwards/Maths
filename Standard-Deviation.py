import numpy as np
import random
import matplotlib.pyplot as plt

def get_sample(pop, size):
    
    sample = random.sample(pop, size)
    length = len(sample)

    mean = sum(sample)/length
    variance = sum([x**2 for x in sample])/length - mean**2

    if size == 1:
        return 1, 1, mean
    
    guess = variance * (length/(length - 1))

    return variance, guess, mean

pop = [random.randint(100, 200) for x in range(1000)] #uniform distribution 
#pop = list(np.random.normal(177.8, 10.16, 1000)) #mu, s, n

pop_variance, other, pop_mean = get_sample(pop, 1000)


fig, ax = plt.subplots(2,2)
variances = []
means = []
sample_size = 10
for i in range(1000):
    value = get_sample(pop, sample_size)
    variances.append(value[1])
    means.append(value[2])

ax[0, 1].set(xlabel="Variances of samples (n={})".format(sample_size))
ax[0, 1].hist(variances, 30)

ax[1, 1].set(xlabel="Mean of samples (n={})".format(sample_size))
ax[1, 1].hist(means, 30)

aves = []
v_aves = []
for k in range(1,1000):
    if k%100==0:print(k)
    variances = []
    means = []
    differences = []
    for i in range(1000):
        value = get_sample(pop, k)
        variances.append(value[1])
        means.append(value[2])
        try:
            differences.append((pop_variance/value[1])*100-100)
            variances.append((pop_variance/value[0])*100-100)
        except ZeroDivisionError:
            differences.append(0) #good enough

    aves.append(abs(sum(differences))/len(differences))
    v_aves.append(abs(sum(variances))/len(variances))

for i in aves:
    if i <= 0.01:
        print("Under 0.01% difference at n =", aves.index(i) + 1)
        break

print("\nPopulation mean:", pop_mean)
print("\nPopulation:", pop)

ax[0, 0].set(title="Distribution")
ax[0, 0].hist(pop, 30, density=True)

ax[1, 0].set(xlabel="sample size", ylabel="expected percentage difference",
             title="Expected vs actual variance")
ax[1, 0].plot(aves[4:]) #Miss out the first 4 due to being very large percentages

f, axe = plt.subplots(1,1)
axe.set(xlabel="sample size", ylabel="variance percentage difference",
             title="Expected vs actual variance")
axe.plot(v_aves[4:])

plt.show()
