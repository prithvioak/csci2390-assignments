from client import count, _pretty_print
from matplotlib import pyplot
import numpy as np

import sys

# Return a random sample from laplace with mean/loc = mu and scale/spread b.
def laplace(mu, b):
  # TODO: implement laplace sampling or use numpy's laplace.
  # epsilon = 0.5
  return np.random.laplace(mu, b)

# Return a noised histogram that is epsilon-dp.
def dp_histogram(epsilon):
  # TODO: Find out the parameters for the noise distribution.
  sensitivity = 1
  mu = 0
  b = sensitivity / epsilon
  
  # Get the exact histogram without noise.
  headers, rows = count(["age", "music"], False)

  # Iterate over counts and apply the laplace noise.
  noised_rows = []
  for (age, music, value) in rows:
    # TODO: compute the noised value.
    # TODO: round the noised_value to the closest integer.
    noised_value = round(value + laplace(mu, b))

    # Append the noised value and associated group by labels.
    noised_rows.append((age, music, noised_value))  

  return headers, noised_rows

# Plot the frequency of counts for the first group
# (age 0 and Hip Hop).
def plot(epsilon):
  ITERATIONS = 150

  # We will store the frequency for each observed value in d.
  d = {}
  most_common = (0,0)
  total = 0
  for i in range(ITERATIONS):
    headers, rows = dp_histogram(epsilon)
    # Get the value of the first row (age 0 and hip hop).
    value = round(rows[0][-1])
    d[value] = d.get(value, 0) + 1
    if d[value] > most_common[1]:
      most_common = (value, d[value])
  total = sum([value * d[value] for value in d.keys()])

  # Turn the frequency dictionary into a plottable sequence.
  vmin, vmax = min(d.keys()) - 3, max(d.keys()) + 3
  xs = list(range(vmin, vmax + 1))
  ys = [d.get(x, 0) / ITERATIONS for x in xs]

  print("Most common value:", most_common[0], "with frequency", most_common[1] / ITERATIONS)
  print("Average value:", total / ITERATIONS)
  # Plot.
  pyplot.plot(xs, ys, 'o-', ds='steps-mid')
  pyplot.xlabel("Count value")
  pyplot.ylabel("Frequency")
  pyplot.savefig('dp-plot-'+str(epsilon)+'.png')

# Run this for epsilon 0.5
if __name__ == "__main__":
  epsilon = 0.5
  if len(sys.argv) > 1:
    epsilon = float(sys.argv[1])

  print("Using epsilon =", epsilon)
  headers, rows = dp_histogram(epsilon)
  _pretty_print(headers, rows)

  # Plotting code.
  print("Plotting, this may take a minute ...")
  plot(epsilon)
  print("Plot saved at 'dp-plot.png'")
