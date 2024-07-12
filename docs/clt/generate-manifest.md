---
layout: page
---
### Generating a Manifest File from SearchAPI for use with the Command Line Transfer

The HuBMAP Command Line Transfer Utility performs a batch transfer of multiple datasets at once by supplying a manifest 
file that includes the HuBMAP IDs of each dataset and, optionally, a pathway to specific resources within a given dataset. 
More information about the HuBMAP-CLT can be found [here](install-hubmap-clt.html). For the case when a user wishes to 
download each dataset returned by a query using the SearchAPI, an optional argument in the URL for certain supported 
endpoints will return the text necessary for a manifest file rather than its usual output. 

#### Creating a Manifest

For general usage of SearchAPI, refer to its <a href="https://smart-api.info/ui/7aaf02b838022d564da776b03f357158">Smart API</a> 
page where you can find a breakdown of its different endpoints as well as example queries. 

The following endpoints support generating a manifest file:

* ```/search```
* ```/<index_without_prefix>/search```
* ```/param-search/<entity_type>```

To geneate a manifest, append the argument `?produce-clt-manifest=true` to the URL. So for ```/search``` for example, using the base SearchAPI URL
"https://search.api.hubmapconsortium.org/v3/", we get "https://search.api.hubmapconsortium.org/v3/search?produce-clt-manifest=true". 

#### Limitations

Adding this argument prevents the endpoint from returning its normal result. Only the manifest will be furnished. Additionally, 
the manifest will be generated without paths specified to individual resources within a given dataset. The entire directory will be included as
denoted by the "/" in the manifest. 

#### Example query and Manifest

The following is an example of a query,the URL given to generate a manifest, and the manifest to be generated:

https://search.api.hubmapconsortium.org/v3/search?produce-clt-manifest=true"

Request body: 

```
{
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "donor.group_name": "Vanderbilt TMC"
          }
        }
      ],
      "filter": [
        {
          "match": {
            "entity_type.keyword": "Dataset"
          }
        }
      ]
    }
  }
}
```

Generated manifest:

```
HBM744.FNLN.846 /
HBM658.VPJK.669 /
HBM592.RPKF.946 /
HBM363.TBHH.346 /
HBM322.XJQZ.894 /
HBM749.MTJC.865 /
HBM722.TVXP.469 /
HBM223.JQLM.452 /
HBM524.KHPH.599 /
```









