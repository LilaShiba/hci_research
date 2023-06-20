from matplotlib.backends.backend_pdf import PdfPages
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

class Scry:
    
    def __init__(self, df, path='my_pandas_plots.pdf'):
        self.df = df
        self.prob_vectors = []
        self.cols_dict = []
        self.pdf_pages = PdfPages(path)

        self.questions = [
            'Freq of Use',
            'Understands User prompts',
            'Weekly Use',
            'Comfort of Use',
            'Watson as Entry Point',
            'First Time Use',
            'Trust in Reply',
            'Expectations Met'
        ]

        self.scatter_plots()
        #self.p_of_k()
        self.index_outliers()
        self.pdf_pages.close()

    def scatter_plots(self):
        cnt = 0
        for col in self.df.columns:
            plt.figure(figsize=(5, 5))
            col_dict = Counter(self.df[col])
            self.cols_dict.append(col_dict)
            x, y = zip(*col_dict.items())
            plt.scatter(x, y)
            #plt.plot(x, y, '-')
            plt.title('Distribution of ' + self.questions[cnt])
            self.pdf_pages.savefig(plt.gcf(), bbox_inches='tight')
            plt.show()
            cnt += 1

    def p_of_k(self):
        cnt = 0
        for col in self.cols_dict:
            x, y = zip(*sorted(col.items()))
            try:
                n = np.sum(y)
            except TypeError:
                continue
            plt.figure(figsize=(5, 5))
            prob_vector = [val/n for val in y]
            plt.scatter(x, prob_vector)
            plt.title("P(k)" + self.questions[cnt])
            self.pdf_pages.savefig(plt.gcf(), bbox_inches='tight')
            plt.show()
            cnt += 1

    def index_outliers(self):
        logs = []
        for col in self.df.columns:
            if self.df[col].dtype == int:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = (self.df[col] >= Q1 - 1.5 * IQR) & (self.df[col] <= Q3 + 1.5 * IQR)
                for idx, x in enumerate(outliers):
                    if not x:
                        logs.append((col, idx))
        return logs




