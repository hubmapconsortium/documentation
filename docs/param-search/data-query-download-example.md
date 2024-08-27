---
layout: page
---
# Example Data Query and Download

## Overview
The combination of the [RESTful parameterized search](index.html) and the [HuBMAP Command Line Transfer Tool](../clt/index.html) provides for an easy way to programatically query HuBMAP data and download the results of the query.

## Description
Below is an example of how to use the [RESTful parameterized search endpoint](index.html) to query for datasets with specific attributes and produce a manifest of datasets to download and how to use the manifest to download all of the data for the referenced Datasets. The parameterized search feature shown in this example is a simple query mechanism that allows quick querying of data via a single RESTful URL call where queried attributes are constrained to exact string matches of a limited set of attributes, where the query is an "AND" filtered query with all attribute matches as terms in the "AND" clause, for example the query `/param-search/datasets?status=Published&dataset_type=CODEX` will return all datasets that are "Published AND a result of a CODEX assay".  If more complex queries are desired use the standard `/search` endpoint which is documented in the [HuBMAP Search API Endpoints](https://smart-api.info/ui/7aaf02b838022d564da776b03f357158).

This example uses the command line tool `curl` to execute queries.  The [Example Data Query and Download Jupyter Notebook]() has this same example using Python.

### Example Query and Download

The following query will return all CODEX (`dataset_type=CODEX`) Datasets run on a Keyence BZ-X800 machine (`metadata.metadata.acquisition_instrument_model=BZ-X800`) where tissue from a spleen was used (`origin_samples.organ=SP`).  See the [RESTful parameterized search page](index.html) for further information on querying dataset, organ (`origin_samples.organ` represents the organ in the query and `SP` is the organ code (organ code list available [here](schema-sample.html#organ-attribute-values)) and dataset metadata fields.

```
 GET https://search.api.hubmapconsortium.org/v3/param-search/datasets?dataset_type=CODEX&metadata.metadata.acquisition_instrument_model=BZ-X800&origin_samples.organ=SP
```

As is, if this query is submitted via HTTP GET it will produce a json Response with an array of dataset objects which match the query.  Adding the `produce-clt-manifest=true` option to this query will instead prduce a list of Dataset IDs pointing to the Datasets that match this query in a format that will be directly usable by the [HuBMAP Command Line Transfer Tool](../clt/index.html).

To run this from the command line and save the results to a file run:
```
curl "https://search.api.hubmapconsortium.org/v3/param-search/datasets?dataset_type=CODEX&metadata.metadata.acquisition_instrument_model=BZ-X800&origin_samples.organ=SP&produce-clt-manifest=true" > dataset-manifest-for-download.out
```

This results in a file that looks like:

```
HBM548.TSMP.663 /
HBM825.PBVN.284 /
HBM558.SRZG.629 /
HBM987.XGTH.368 /
HBM647.MFQB.496 /
HBM244.TJLK.223 /
HBM633.CLVN.674 /
HBM427.SMGB.866 /
. . .
```

To use the HuBMAP CLT tool to download the data from these datasets:

  - Install the Globus Connect Personal client and the HuBMAP CLT per the [HuBMAP CLT Setup Instructions](../clt/install-hubmap-clt.html)
    - Python 3.9 or greater is required for the HuBMAP CLT, install from the [Python Downloads page](https://www.python.org/downloads/)
    - Setup Note: A common issue arrises between the configuration of the GCP client and HuBMAP CLT.  By default HuBMAP CLT stores files in the user's home directory under a directory called `hubmap-downloads`, so make sure to configure the GCP client by goint to "Preferences"-->"Access" and adding the `hubmap-downloads` directory in the user's home like (Example shown is Mac OS X):<br/>
    <img src="/images/globus-properties.png" alt="HuBMAP Provenance" width="400"/>
  - On the command line log into the HuBMAP Globus server using:
  ```
  hubmap-clt login
  ```
  Globus login screen will open in your default web browser.  Follow the instructions to log in.  For publicly available HuBMAP data any login will work (your institution, Google, GitHub, etc..).
  - Download the data using the manifest file genrated above:
  ```
  hubmap-clt transfer dataset-manifest-for-download.out
  ```

Futher instructions on the usage of the HuBMAP CLT are available on the main [HuBMAP Command Line Transfer Tool page](../clt/index.html)