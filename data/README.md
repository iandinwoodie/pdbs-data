# Data

This directory contains various stages of the data set as it was transformed
from its raw to final form. Brief descriptions of each stage are provided below
in order from least to most modified.

## Stage 0: Raw Data

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

## Stage 1: Structured Data

The structured data is a restructuring of the raw data for ease of analysis. In
its new form, the layout of the data can be summarized with the following table:

| owner-id | dog-id | event-1    | event-2    |
| -------- | ------ | ---------- | ---------- |
| owner-1  | dog-1  | event-data | event-data |
| owner-1  | dog-2  | event-data | event-data |
| owner-2  | dog-1  | event-data | event-data |

Each row represents a complete entry (i.e., both event 1 and event 2 responses)
for a single dog. Incomplete entries were dropped from the data set.
