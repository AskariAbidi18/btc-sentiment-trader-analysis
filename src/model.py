import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def run_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    rf_model = RandomForestClassifier(n_estimators = 100, random_state = 42)

    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    importances = rf_model.feature_importances_

    feature_importance_df = pd.DataFrame({
        'feature': X.columns,
        'importance': importances
    })

    feature_importance_df = feature_importance_df.sort_values(by='importance', ascending=False)

    print("\nTop Feature Importances:")
    print(feature_importance_df.head(10))

    feature_importance_df.head(10).plot(
        kind='barh',
        x='feature',
        y='importance',
        title='Top Feature Importances'
        )
    plt.gca().invert_yaxis()
    plt.show()
