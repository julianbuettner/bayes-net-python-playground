# Bayes Net Playground

## Don't use

This repository is used as extended pastebin.

## How to use

Check out `main.py`.  
No dependencies required.

## Demo output
Output of `./main.py`:
```
=========
Sprinkler
Rain     = 0   #  0.400 0.600
Rain     = 1   #  0.010 0.990

====
Rain
   #  0.200 0.800

=========
Grass Wet
Rain     = 0 | Sprinkle = 0   #  0.000 1.000
Rain     = 0 | Sprinkle = 1   #  0.800 0.200
Rain     = 1 | Sprinkle = 0   #  0.900 0.100
Rain     = 1 | Sprinkle = 1   #  0.990 0.010

Inference run. Calculated nodes: 2
Inference run. Calculated nodes: 0
Done
Value 0.32000000000000006
```

![](https://en.wikipedia.org/wiki/Bayesian_network#/media/File:SimpleBayesNet.svg)
