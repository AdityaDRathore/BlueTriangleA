import numpy as np

class PCA:
    def __init__(self, n_dependcies):
        self.n_dependcies = n_dependcies
        self.mean = None
        self.components = None

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        cov = np.cov(X.T)
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        idx = np.argsort(-eigenvalues)
        self.components = eigenvectors[:, idx[:self.n_dependcies]]
        
    def transform(self, X):
        X_centered = X - self.mean
        return np.dot(X_centered, self.components.T)