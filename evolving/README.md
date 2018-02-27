# xStream Datasets - Evolving Streams

[https://cmuxstream.github.io](https://cmuxstream.github.io)

## Sources and Preprocessing

Original dataset obtained from [StreamSpot](https://github.com/sbustreamspot/sbustreamspot-data). Each
line (shingle) of the original dataset corresponds to a pair of shingles, one added and one removed from the graph.
The shingles are obtained by modifying the
[StreamSpot shingle construction code](https://github.com/sbustreamspot/sbustreamspot-train/tree/master/graphs-to-shingle-vectors).

## Format

All files are in a modified SVM-light format; each line is formatted as follows:

```
label shingle_id:count shingle_id:count ... graph_id
```

The evolving stream as incoming and outgoing shingles for each system call are contained in `flash-stream.gz` and
`java-stream.gz`. The entire graphs as a row-stream are contained in `flash-static.gz` and `java-static.gz` for
convenience (to test with iForest or other static methods).

Graph ID's correspond to scenarios as follows:

   1. YouTube (graph ID's 0 - 99)
   2. GMail (graph ID's 100 - 199)
   3. VGame (graph ID's 200 - 299)
   4. Flash drive-by-download attack (graph ID's 300 - 399)
   5. Download (graph ID's 400 - 499)
   6. CNN (graph ID's 500 - 599)
   7. Java attack (graph ID's 600 - 699)

# Contact

   * emaad@cmu.edu
   * hlamba@andrew.cmu.edu
   * lakoglu@andrew.cmu.edu
