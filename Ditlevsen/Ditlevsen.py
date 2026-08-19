import numpy as np


def probability_intersection(pe, correlation_matrix):
    k = len(pe)
    intersection_matrix = np.zeros([k,k])
    for i in range(k):
        for j in range(k):
            intersection_matrix[i,j] = pe[i]*pe[j]+correlation_matrix[i,j]*(pe[i]*(1-pe[j])*pe[j]*(1-pe[i]))
    return intersection_matrix


def Ditlevsen_lower_bound(pe_sorted, intersection_matrix_sorted):
    result = pe_sorted[0]  # P(E1)
    k = len(pe_sorted)
    
    for i in range(1, k):  
        sum_intersections = np.sum(intersection_matrix_sorted[i, :i])
        result += max(pe_sorted[i] - sum_intersections, 0.0)
    
    return result



def Ditlevsen_upper_bound(pe_sorted, intersection_matrix_sorted):
    sum_all = np.sum(pe_sorted)  # Sum of all P(Ei)
    sum_max_intersections = 0.0
    k = len(pe_sorted)
    
    for i in range(1, k):
        max_intersection = np.max(intersection_matrix_sorted[i, :i])
        sum_max_intersections += max_intersection
    return sum_all - sum_max_intersections



if __name__ == "__main__":
    pe = np.array([1.2e-5, 1.6e-5, 1.35e-5, 1.5e-5]) # and example of P(events)
    correlation_matrix = np.array([[0.31, 0.37, 0.4,  0.41],
    [0.37, 0.25, 0.31, 0.36],
    [0.4,  0.31, 0.21, 0.37],
    [0.41, 0.36, 0.37, 0.26]]) # just a random correlation matrix

    intersection_matrix = probability_intersection(pe, correlation_matrix=correlation_matrix)

    # all the following variables must be sorted with the same indexing
    pe_sorted = np.sort(pe)[::-1]
    idx = np.argsort(pe)[::-1]
    correlation_matrix_sorted = correlation_matrix[np.ix_(idx, idx)]
    intersection_matrix_sorted = intersection_matrix[np.ix_(idx, idx)]

    print('Ditlevsen lower bound= ', Ditlevsen_lower_bound(pe_sorted, intersection_matrix_sorted))
    print('Ditlevsen upper bound= ', Ditlevsen_upper_bound(pe_sorted, intersection_matrix_sorted))
