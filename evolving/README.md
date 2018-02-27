# xStream Datasets - Evolving Streams

[https://cmuxstream.github.io](https://cmuxstream.github.io)

## Sources and Preprocessing

The original dataset was obtained from [StreamSpot](https://github.com/sbustreamspot/sbustreamspot-data). A copy is
stored in this repository as `streamspot-raw.gz`. Refer to the original repository for details.

Each line (system call) of the original dataset corresponds to
shingles that are added and removed from a graph. These shingles are obtained by modifying the
[StreamSpot shingle construction code](https://github.com/sbustreamspot/sbustreamspot-train/tree/master/graphs-to-shingle-vectors)
with the `chunk-length` parameter set to 50.

Each shingle is mapped to a shingle ID for convenient representation in the SVM-light format, though this is not
a requirement for xStream. The raw shingles are present in `shingles.gz`, with the shingle ID implied by the line
number (starting from zero).

## Format

The evolving stream as incoming and outgoing shingles for each system call is contained in `streamspot-stream.gz`.
The file is in a modified SVM-light format; each line is formatted as follows:

```
graph_id incoming_shingle_id:1 incoming_shingle_id:1 ... outgoing_shingle_id:-1 outgoing_shingle_id:-1 ...
```

A row-stream version of the dataset with complete graphs (shingle vectors) is contained in `streamspot-static.gz`
for convenience (to test with iForest or other static methods). The graph ID is implied by the line number
(starting from zero). The file is in the SVM-light format, with each line formatted as:

```
anomaly_label shingle_id:count shingle_id:count ...
```

Graph ID's correspond to scenarios as follows:

   1. YouTube (graph ID's 0 - 99)
   2. GMail (graph ID's 100 - 199)
   3. VGame (graph ID's 200 - 299)
   4. Flash drive-by-download attack (**anomaly**) (graph ID's 300 - 399)
   5. Download (graph ID's 400 - 499)
   6. CNN (graph ID's 500 - 599)
   7. Java attack (**anomaly**) (graph ID's 600 - 699)

## Example

The included `test_iforest_streamspot.py` script runs iForest on the StreamSpot datasets, testing detection of either
the Flash or Java attack against one or all benign scenarios. See the above section for the mapping from
scenario numbers to benign scenarios.

```
python test_iforest_streamspot.py <path to streamspot-static> <attack, "flash" or "java"> <scenario, index or "all">
```

Example runs:
```
python test_iforest_streamspot.py ./streamspot-static java all # Java vs. all
python test_iforest_streamspot.py ./streamspot-static flash 5 # Flash vs. Download
```

# Contact

   * emaad@cmu.edu
   * hlamba@andrew.cmu.edu
   * lakoglu@andrew.cmu.edu
