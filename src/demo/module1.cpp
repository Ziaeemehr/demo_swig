#include "module1.hpp"
#include <numeric>

double compute_average(const std::vector<double> &values)
{
    if (values.empty())
        return 0.0;
    double sum = std::accumulate(values.begin(), values.end(), 0.0);
    return sum / values.size();
}

double compute_sum(const std::vector<double> &values)
{
    if (values.empty())
        return 0.0;
    double sum = std::accumulate(values.begin(), values.end(), 0.0);
    return sum;
}
