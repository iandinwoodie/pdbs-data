# Raw Data

The raw data is a dump of collected responses from the eletronic data capture
(EDC) platform REDCap. Each row of the raw data represents a user response for
a single event. The survey consisted of two events:

1. Gathering information on the presence of behavior problems for up to 5 dogs.
2. Gathering information on the pursued paths of treatment, if any, for the dogs
   that exhibited problematic behavior.

From a high level, the layout of this data can be summarized with the following
table:

| owner-id | event-id | dog-1    | dog-2    | dog-3    | dog-4    | dog-5    |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| owner-1  | event-1  | dog-data | dog-data | dog-data | dog-data | dog-data |
| owner-1  | event-2  | dog-data | dog-data | dog-data | dog-data | dog-data |
| owner-2  | event-1  | dog-data | dog-data | dog-data | dog-data | dog-data |
