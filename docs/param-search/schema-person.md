---
layout: page
---

# HuBMAP Person schema

## Overview:
This page describes the Person schema for HuBMAP data. Person data occurs in the Donor, Sample or Dataset schemas.
```
GET https://search.api.hubmapconsortium.org/param-search/donors?group_name=Stanford TMC&descendants.organ=LI
```

### Person Schema

| Attribute                | Type     | Description                                           |
|--------------------------|----------|-------------------------------------------------------|
| first_name               | string   | The full name of the person.                          |
| last_name                | string   | The last name of the person.                          |
| middle_name_or_initial   | string   | The middle name or initial of the person.             |
| orcid_id                 | string   | The ORCID iD of the person.                           |
| affiliation              | string   | The institution that the person is affiliated with.   |
