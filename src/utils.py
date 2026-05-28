# Utility functions for Student Performance Predictor


def performance_category(score):
    """
    Categorize student performance
    based on predicted score
    """

    # Excellent performance
    if score >= 80:
        return 'Excellent'

    # Average performance
    elif score >= 60:
        return 'Average'

    # Needs improvement
    else:
        return 'Needs Improvement'