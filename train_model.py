import numpy as np
import pandas as pd
import re

df = pd.read_csv("train_data.csv")

def get_features(url : str):
    Length = len(url)
    n_dots = sum(1 for c in url if c == '.')
    n_special = sum(1 for c in url if not c.isalnum())
    n_digits = sum(1 for c in url if c.isdigit())
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    has_ip = 1 if re.search(ip_pattern, url) else 0
    features = np.array([Length, n_dots, n_special, n_digits, has_ip])
    return features

def prepare_input(data = df):
    X_raw = df['url'].values
    y = df['label'].values
    X_features = np.array([get_features(url) for url in X_raw])
    return X_features , y

def plotting():
    import matplotlib.pyplot as plt
    import seaborn as sns
    X, y = prepare_input()
    feature_names = ['Length', 'Num_Dots', 'Num_Special', 'Num_Digits', 'Has_IP']
    X_df = pd.DataFrame(X, columns=feature_names)
    X_df['Label'] = y

    plt.figure(figsize=(12, 8))
    for i, feature in enumerate(feature_names):
        plt.subplot(2, 2, i + 1)
        sns.histplot(data=X_df, x=feature, hue='Label', multiple='stack', bins=30)
        plt.title(f'Distribution of {feature} by Label')
    plt.show()


if __name__ == "__main__":
    X , y = prepare_input()
    print(X)    
    print(y)
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    import joblib
    joblib.dump(model, "phish_model.pkl")

