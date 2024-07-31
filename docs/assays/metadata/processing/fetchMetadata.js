#!/usr/bin/env node
var fs = require('fs');

var assayURLs = ```
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F63c06fb2-4638-4979-aa97-5aff2a840156", // 10X Multiome
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fc9c6a02b-010e-4217-96dc-f7ef71dd14c4", // AF (Auto-fluorescence)
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fdd5e8653-81cf-470b-b71b-15cab421bb84", // ATACseq
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F47c6071a-2ec7-46c1-94d9-6b5e2d7ac982", // CODEX
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F3829a2c4-e29b-4dca-91f2-af3d427ed57b", // Confocal
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F01d909d8-84a8-4362-9e42-782bc4da0eec", // DESI
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F609c3adb-e65d-4124-bb1b-dd937f231850", // Enhanced SRS
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F0310a026-4aed-49a5-a806-e3a281351d8a", // HiFi-Slide
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F907d89c7-6cf4-4ec6-9edd-63cf0441d689", // Histology
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fef090376-4e19-43cb-92c1-91a1d758ee6e", // LC-MS
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fa4ff738c-a7e9-40c1-966e-22cf9c885fad", // Light Sheet
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fce5524be-dab6-4668-97c1-8a5a09325e5f", // 2D IMC
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F2e35434f-e6ed-4e01-a54a-189ec0706a3d", // MALDI
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Ff1ef260f-d4a3-43db-a739-49b394aeee20", // MERFISH
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F784cfaa7-4a73-4173-b639-b24e0ed76155", // MIBI
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F5efe0d51-828c-457a-9b94-2ac8090fe14f", // MUSIC
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F62af6829-743d-423e-a701-204710e56beb", // PhenoCycler
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F944e5fa0-f68b-4bdd-8664-74a3909429a9", // RNAseq
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fe4df583f-95df-4113-92dc-6e9b90124d9f", // RNAseq (with probes)
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fe75faf85-125a-403e-80ee-21d4e7d80edc", // Second Harmonic Generation
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F2c32e88f-f8b5-42dc-85dd-1298e851da9d", // SIMS
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fb76e54fe-5352-449b-9188-f250b51fbedc", // SnareSeq2
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F80320147-a111-45da-9611-0eab83f594b3", // Thick Section Multiphoton MxIF
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2F4646ec9d-f3c9-4619-bc45-7e14748bb976", // Visium (with probes)
  "https://open.metadatacenter.org/templates/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fbabf1e69-f0eb-479a-bdc5-b70199669675", // Visium (no probes)
```

var stripOut = ```
  "@context",
  "@id",
  "@type",
  "schema:isBasedOn",
  "schema:name",
  "schema:description",
  "pav:derivedFrom",
  "pav:createdOn",
  "pav:createdBy",
  "pav:lastUpdatedOn",
  "oslc:modifiedBy",
```

async function fetchData(url){
  const response = await fetch(url);
  const data = await response.json();
  return data;
}
function callback(){
  console.log("file created")
}

function processAssays(){
  var assays = ``````;
  for (var i = 0; i < assayURLs.length; i++){
    fetchData(assayURLs```i```).then(assay => {
      assay;
      var props = assay```"properties"```;
      var assayDetails = {
        assayName : assay```"schema:name"```,
        properties : ``````
      }
      for (const property in props) {
        if (!stripOut.includes(property)) {
          var name = props```property``````"skos:prefLabel"```
          var shortcode = props```property``````"schema:name"```
          var value = ""
          var type = props```property``````"_ui"``````"inputType"```
          if(type === 'radio'){
            type = 'ENUM'
            value = 'ENUM'
          }else{
            type = props```property``````"_ui"``````"inputType"```
            value = ''
          }
          assayDetails.properties.push({
            attribute:shortcode,
            label:name, 
            type: type,
            description: props```property``````"schema:description"```,
            value: value,
            required: props```property``````"_valueConstraints"``````'requiredValue'```,
            // regex: props```property``````"_valueConstraints"``````'regex'```,
            // required: reqs.includes(property),
          });
        }
      }
      
      assays.push(JSON.stringify(assayDetails))
      var title = assay```'schema:name'```+'.json'
      title = title.replace(/```\s;```+/g, "-")
      fs.writeFile("./json/"+title, JSON.stringify(assayDetails), callback);
      fs.writeFile("./metaJSON/"+title, JSON.stringify(assayDetails.properties), callback);
    });
  }
}

processAssays();



