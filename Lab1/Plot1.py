from collections import Counter
import Lab1
import matplotlib.pyplot as plt

spam_com = dict(Counter(Lab1.dict_spam).most_common(10))
ham_com = dict(Counter(Lab1.dict_ham).most_common(10))


fig1, gr1 = plt.subplots()
gr1.plot(spam_com.keys(), spam_com.values(),  label='spam', color='red')
gr1.set_xlabel('Слова')
gr1.set_ylabel('Количество')
plt.legend()
plt.show()


fig2, gr2 = plt.subplots()
gr2.plot(ham_com.keys(), ham_com.values(),  label='ham', color='blue')
gr2.set_xlabel('Слова')
gr2.set_ylabel('Количество')
plt.legend()
plt.show()
