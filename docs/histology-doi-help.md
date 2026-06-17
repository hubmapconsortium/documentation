---
layout: doi-help-page
title: Metadata Reporting Standards - Documents Provided
permalink: /histology-doi-help/
---

<h1>Metadata Reporting Standards</h1>
<p class="spec-name">Documents Provided</p>

<div class="help-intro">
  <p>The HuBMAP Metadata Reporting Standards include schemas for both descriptive and structural metadata. The descriptive metadata provides a standardized description of samples, experiments, and processing context. The structural metadata provides standardized file organization, including hierarchical file and directory specifications, file type and naming conventions.</p>

  <p>The standards vary slightly by experiment type, but they are all delivered using the same core archive pattern: JSON metadata, XLSX metadata, TSV metadata, MD files for folder and file organization, and ZIP files for directories.</p>
</div>

<section class="help-card">
  <article class="help-file">
    <h2><span class="help-file-name">metadata.jsonld</span> <small class="help-file-type">(JSON-LD file)</small></h2>
    <h3>JSON Metadata Schema Description</h3>
    <p>This JSON schema defines the structure and validation rules for metadata instances generated from a metadata template in the CEDAR framework. It is produced by the CEDAR Workbench and reflects the template's OpenView representation.</p>
    <p>The schema follows JSON Schema conventions and includes a JSON-LD context so each field has semantic meaning. It defines the available properties, required fields, data types, and validation constraints used to check submitted metadata.</p>
    <p>Each schema supports template metadata, field definitions, validation constraints, and the UI configuration used to render metadata entry forms.</p>
  </article>

  <article class="help-file">
    <h2><span class="help-file-name">deprecated.json</span> <small class="help-file-type">(JSON file)</small></h2>
    <h3>Deprecated List</h3>
    <p>This file tracks field names that have been retired across the schema history. When a field is removed from any schema version, it is added here so the list becomes an accumulating record of retired fields, not just the current version.</p>
    <p>It helps consumers identify legacy fields that may still appear in older datasets even though they are no longer supported by the current schema.</p>
  </article>

  <article class="help-file">
    <h2><span class="help-file-name">metadata.yml</span> <small class="help-file-type">(YAML file)</small></h2>
    <h3>YAML Metadata Schema Description</h3>
    <p>This file provides a simplified YAML version of the descriptive metadata schema. It is intended to be easier for humans to read while still preserving a structured format that can be used computationally.</p>
  </article>

  <article class="help-file">
    <h2><span class="help-file-name">metadata.xlsx</span> <small class="help-file-type">(Microsoft Excel file)</small></h2>
    <h3>Excel Spreadsheet Template Description</h3>
    <p>The Excel template is generated from a CEDAR metadata template and is designed for bulk submission workflows. It offers a table-based format for collecting multiple records and includes supporting sheets for permitted values and standardized term identifiers.</p>
    <p>Those supporting sheets feed the dropdown choices in the data-entry sheet, which helps users select valid terms consistently, reduce manual entry errors, improve data quality, and make bulk submission easier.</p>
    <p>The template is compatible with the Metadata Spreadsheet Validator, which can be used to verify records before submission.</p>
  </article>

  <article class="help-file">
    <h2><span class="help-file-name">metadata.tsv</span> <small class="help-file-type">(tab-separated values file)</small></h2>
    <h3>Tab-Separated Values Template Description</h3>
    <p>The TSV template is also generated from a CEDAR metadata template and is intended for bulk submission in a lightweight, machine-readable format. It provides one row per record, with each column corresponding to a metadata field in the template.</p>
    <p>Like the spreadsheet version, it is compatible with the Metadata Spreadsheet Validator for checking the correctness of bulk metadata records before submission.</p>
  </article>

  <article class="help-file">
    <h2><span class="help-file-name">directory.md</span> <small class="help-file-type">(markdown file)</small></h2>
    <h3>Markdown Structural Metadata Description</h3>
    <p>This markdown file documents the structural metadata schema specification and is organized into three parts:</p>
    <ul>
      <li><strong>File Organization Schema:</strong> a table of hierarchical file and directory specifications, including file type, naming conventions, and required status.</li>
      <li><strong>Directory Tree:</strong> a more human-readable view of the directory structure.</li>
      <li><strong>YAML:</strong> a YAML version of the file organization schema that can be used with the HuBMAP Ingest Validation Tools.</li>
    </ul>
  </article>

  <article class="help-file">
    <h2><span class="help-file-name">empty_tree.zip</span> <small class="help-file-type">(ZIP archive)</small></h2>
    <h3>ZIP Archive Description</h3>
    <p>This archive contains the empty directory structure without any files. It preserves the metadata standards' hierarchical folder layout and, when unzipped, creates the dataset-specific directory tree on the destination system.</p>
    <p>The archive can be used as a framework for structuring files so they conform to the dataset-specific file hierarchy standard.</p>
  </article>
</section>
