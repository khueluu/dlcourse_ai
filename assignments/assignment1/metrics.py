def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for y_pred, y_true in zip(prediction, ground_truth):
        if y_pred == y_true:
            if y_pred == True:
                TP +=1
            else:
                TN +=1
        else:
            if y_pred == True:
                FP +=1
            else:
                FN +=1    
    # print(TP, TN, FP, FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    accuracy = (TP + TN) / len(ground_truth)
    f1 = (2 * precision * recall) / (precision + recall)

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = sum(ground_truth == prediction)/prediction.shape[0]
    return accuracy
