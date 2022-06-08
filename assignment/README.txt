There are 3 parts of codes:
	-simple classifier source code(Bayes.py, DT.py, k-nn.py, MLP.py)
	-ensemble classifier source code(ensemble_xxxxx.py)
	-a testing source code(testing.py)
	-a plotting source code(plot_new.py)

Before you run any code, make sure that there is a "spamBase" folder outside of current folder(codes folder)
The "spamBase" folder should contains these files:
	-spambase.data
	-spambase.DOCUMENTATION
	-spambase.names

If you want to test my code, the testing logic is :
1. run Bayes.py, DT.py, k-nn.py and MLP.py
2. run ensemble_voting.py
3. run testing.py
4. run ensemble_xxxx.py
5. run testing.py again to test other ensemble classifiers

@Arthor Yuchen Song
e-mail: wisyc@mail.scut.edu.cn or yuchensong@berkeley.edu
