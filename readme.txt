Introduction
- The aim of this work is to implement network simplification technique.Its main purpose is to filter out complex networks by keeping only the main representative links. Minimum Spanning Tree (MST) and Planar Maximally Filtered Graph (PMFG) are alternative techniques. 
The main difference between the PMFG and the MST is that the PMFG will retain a bit more information: If n is the number of nodes, then the MST has n - 1 edges whereas the PMFG has 3(n - 2) edges (compared to the n(n-1)/2 of the complete graph K_n). Besides, the MST is always contained in the PMFG. 
- Networks are visualized using plotly and networkx package.

Test case
- investor networks
- simulated network

Requirement and install
- planarity

References
Tumminello, M., Aste, T., Di Matteo, T., & Mantegna, R. N. (2005). A tool for filtering information in complex systems. Proceedings of the National Academy of Sciences of the United States of America, 102(30), 10421-10426.
https://gmarti.gitlab.io/networks/2018/06/03/pmfg-algorithm.html
https://github.com/hagberg/planarity
http://jgaa.info/accepted/2004/BoyerMyrvold2004.8.3.pdf
https://networkx.github.io/documentation/stable/index.html

