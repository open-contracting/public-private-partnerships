# Framework reference

```eval_rst
.. image:: _static/images/disclosure-framework.png
```

[The World Bank Framework for Disclosure in Public Private Partnership Projects](http://www.worldbank.org/en/topic/publicprivatepartnerships/brief/ppp-tools#T1) provides a comprehensive overview of motivations, processes and legal frameworks for disclosure of information in Public Private Partnership projects. 

This section provides a step-by-step reference resource on how all the requirements from the disclosure template in the framework can be captured as structured data and documents using OCDS for PPPs. Individual implementations of the framework may vary with respect to the elements of disclosure they prioritize. 

This section should be read in conjunction with the Disclosure Framework.

The mapping for each requirement in the framework includes a guide to publication timing, indicating whether information should be **P**ublished, **R**epeated or **U**pdated at each stage of the contracting process. More information on the stages of the contracting process can be found in the [publication timing section](timing.md).

## I. Basic Project Information 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   R   R   R   R   R 
==  ==  ==  ==  ==  ==

```

</div>

### I.1. Name, location and sector 

Each project should have a name, location and sectoral classification.

This information is included in the `planning/project` section of each release. A detailed breakdown of each field is given below. 

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/planning/project
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/planning/project
  :ignore_path: /releases/0/
```

</div>

#### I.1.1. Project name and description 

These titles and descriptions can be used by applications in summary lists, so should be kept concise and jargon free.

We recommend keeping descriptions to one paragraph or less. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: planning/project/title,planning/project/description
    :collapse: 
    :nocrossref:
```

#### I.1.2. Project sector 

Projects should be classified using the UN Classification of the Functions of Government Scheme (COFOG).

This can be cross-walked to most other PPP classification schemes in use, and so provides a common framework for understanding the sectoral focus of investments. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: planning/project/sector
    :collapse: 
    :nocrossref:
```

##### I.1.2.1. Project sector (additional) 

One or more additional project classifications can be provided if required by a particular user of the data, or to relate the project to a national taxonomy. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: planning/project/additionalClassifications
    :collapse: 
    :nocrossref:
```

Additional classification schemes can also be provided, such as project classification against the Sustainable Development Goals (SDGs), or against national frameworks. 

#### I.1.3. Project location 

The locations where a project is taking place can be specified using:

* **A gazetteer entry**. For example, the GeoNames code of the administrative division where activity is taking place.
* **A GeoJSON object**. Describing the boundary, or extent, of where activity will take place.

There are a range of tools available to generate GeoJSON data, such as [http://geojson.io/](http://geojson.io) 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: planning/project/locations
    :collapse: 
    :nocrossref:
```

### I.2. Sponsoring agency/department 

#### I.2.1. Organization details 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

Details of the sponsoring agency or department, including name and contact details, should be provided using an [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) object in the [parties](../reference/schema/#release-schema.json,,parties) array. The party's `roles` array should include the 'publicAuthority' code, and the party's `contactPoint` field can be used to provide details of a named representative.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/parties/1
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/parties/1
  :ignore_path: /releases/0/
```

</div>

#### I.2.2. Organization reference 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

A reference to the sponsoring agency or department should be provided using an [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) object in the [publicAuthority](../reference/schema/#release-schema.json,,publicAuthority) field, referencing the relevant entry in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/publicAuthority
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/publicAuthority
  :ignore_path: /releases/0/
```

</div>

### I.3. Project value 

The value of a project can be specified at a number of points in time. 

#### I.3.1. Planned value 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   R   R   R       R 
==  ==  ==  ==  ==  ==

```

</div>

The value, or range of values, anticipated during the planning stage. 

**Schema**: Information can be provided using a [Value](https://standard.open-contracting.org/1.1/en/schema/reference/#value) object in the [planning/project/totalValue](../reference/schema/#release-schema.json,,planning/project/totalValue) field.

#### I.3.2. Tender value 

The value, or range of values, in a call for tenders for the project. 

**Schema**: Information can be provided using a [Value](https://standard.open-contracting.org/1.1/en/schema/reference/#value) object in the [tender/value](../reference/schema/#release-schema.json,,tender/value) field.

#### I.3.3. Award value 

The value of the project at time of contract award. 

**Schema**: Information can be provided using a [Value](https://standard.open-contracting.org/1.1/en/schema/reference/#value) object in the [awards/value](../reference/schema/#release-schema.json,,awards/0/value) field.

#### I.3.4. Contract value 

The total value of the project agreed in the contract(s). 

**Schema**: Information can be provided using a [Value](https://standard.open-contracting.org/1.1/en/schema/reference/#value) object in the [contracts/value](../reference/schema/#release-schema.json,,contracts/0/value) field.

### I.4. Project economic and social benefits 

Project need: benefits provided, economic and social (including specific information on the public interest aspect)

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

Information on the project need, benefits provided, and economic and social impact should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

Links to these documents should be provided using [Document](reference/documents) objects in the [planning/documents](../reference/schema/#release-schema.json,,planning/documents) array. Each document's `documentType` field should be set to 'needsAssessment'.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/planning/documents/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/planning/documents/0
  :ignore_path: /releases/0/
```

</div>

### I.5. Project technical description 

Technical description of the physical infrastructure

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

A technical description of the physical infrastructure should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

Links to these documents should be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. Each document's `documentType` field should be set to 'technicalSpecifications'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### I.6. Project high level description 

High-level description of the services

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

A high-level description of the services should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

Links to these documents should be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. Each document's `documentType` field should be set to 'serviceDescription'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### I.7. Estimated project demand 

Estimated demand to be served annually

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

#### I.7.1. Structured information on estimated demand 

Structured data about estimated demand should be provided in the `planning/forecast` section, using an array of metrics building blocks.

A metric with the `id` 'demand' should be given, with a series of forecast `observations` that capture the estimated demand for a given period.

These estimates can be disaggregated by any number of dimensions contained as key-value pairs within the `observation/dimensions` object. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: planning/forecasts
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/planning/forecasts
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/planning/forecasts
  :ignore_path: /releases/0/
```

</div>

#### I.7.2. Estimated demand documentation 

Non-structured data relating to estimated demand can be provided through:

* A short summary text
* A link to one or more documents that provide additional information

Links to these documents should be provided using [Document](reference/documents) objects in the [planning/documents](../reference/schema/#release-schema.json,,planning/documents) array. Each document's `documentType` field should be set to 'estimatedDemand'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### I.8. Project additionality 

Project additionality

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

Information on the project additionality should be provided through planning documents containing:

* A short summary text
* A link to one or more documents that provide additional information

Descriptions should be provided for both:

* The additionality of the project;
* The additionality of the finance method used;

Links to these documents should be provided using [Document](reference/documents) objects in the [planning/documents](../reference/schema/#release-schema.json,,planning/documents) array. Each document's `documentType` field should be set to 'projectAdditionality' or 'financeAdditionality'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### I.9. Reasons for selection of PPP mode (general) 

Reason for selection of PPP mode and type in brief

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

A short summary of the reason for the PPP selection mode should be provided through:

* A short summary text
* A link to one or more documents that provide additional information

Links to these documents should be provided using [Document](reference/documents) objects in the [planning/documents](../reference/schema/#release-schema.json,,planning/documents) array. Each document's `documentType` field should be set to 'pppModeRationale'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### I.10. Project approval dates 

Dates of various approvals

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P                     
==  ==  ==  ==  ==  ==

```

</div>

Each approval during the planning stage should be provided as a [Milestone](https://standard.open-contracting.org/1.1/en/schema/reference/#milestone) object in the [planning/milestones](../reference/schema/#release-schema.json,,planning/milestones) array with:

* its `type` field set to 'approval'
* its `dueDate` field set to the date for which the approval is scheduled
* its `status` field set to 'scheduled' or 'met'
* its `dateMet` field set to the date on which the approval was given
* its `documents` array set to any documentation associated with the approval

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/planning/milestones/1
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/planning/milestones/1
  :ignore_path: /releases/0/
```

</div>

### I.11. Contract milestones

Key events relating to commercial and financial close

This information can be provided as [Milestone](https://standard.open-contracting.org/1.1/en/schema/reference/#milestone) objects in the [contracts/milestones](../reference/schema/#release-schema.json,,contracts/0/milestones) array, each with its `type`, `code` and `status` fields set to codes from the relevant codelists and its `documents` array set to links to any additional documentation.

#### I.11.1. Contract milestones - Date of commercial close 

Contract Milestones (Estimated and Actual) - Date of commercial close

> In a financing, the point at which the commercial documentation has been executed but before conditions precedent have been satisfied or waived; before financial close. ([Source](https://pppknowledgelab.org/glossary#Commercial_Close))

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U         
==  ==  ==  ==  ==  ==

```

</div>

This milestone should have a `type` of 'financing', a `code` of 'commercialClose' and a status of either `scheduled` or `met` with either the date that this milestone was achieved in `dateMet`, or the scheduled date in `dueDate`.

**Example**: See [section I.10](#i-10-project-approval-dates) for JSON and flattened examples of the `milestones` building block.

#### I.11.2. Contract milestones - Date of financial close 

Contract Milestones (Estimated and Actual) - Date of financial close

> In a financing, the point at which the documentation has been executed and conditions precedent have been satisfied or waived. Drawdowns become permissible after this point. ([Source](https://pppknowledgelab.org/glossary#Financial_Close))

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U         
==  ==  ==  ==  ==  ==

```

</div>

To indicate the date of financial close, a milestone should be added to the `contract/milestones` (the contract may have a `status` of 'pending' up until it is signed). 

The milestone should have a `type` of 'financing', a `code` of 'financialClose' and a status of either `scheduled` or `met` with either the date that this milestone was achieved in `dateMet`, or the scheduled date in `dueDate`.

**Example**: See [section I.10](#i-10-project-approval-dates) for JSON and flattened examples of the `milestones` building block.

### I.12. Implementation milestones 

Key events relating to the implementation of the project.

This information can be provided as [Milestone](https://standard.open-contracting.org/1.1/en/schema/reference/#milestone) objects in the [contracts/milestones](../reference/schema/#release-schema.json,,contracts/0/milestones) array, each with its `type`, `code` and `status` fields set to codes from the relevant codelists and its `documents` array set to links to any additional documentation.

#### I.12.1. Implementation milestones - Date of commencement of construction or development 

Contract Milestones (Estimated and Actual) - Date of commencement of construction or development

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

The milestone should have a `type` of 'delivery', a `code` of 'developmentStarted' or 'constructionStarted' and a status of either `scheduled` or `met` with either the date that this milestone was achieved in `dateMet`, or the scheduled date in `dueDate`.

**Example**: See [section I.10](#i-10-project-approval-dates) for JSON and flattened examples of the `milestones` building block.

#### I.12.2. Implementation milestones - Date of completion of construction or development 

Contract Milestones (Estimated and Actual) - Date of completion of construction or development

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

The milestone should have a `type` of 'delivery', a `code` of 'developmentComplete' or 'constructionComplete' and a status of either `scheduled` or `met` with either the date that this milestone was achieved in `dateMet`, or the scheduled date in `dueDate`.

**Example**: See [section I.10](#i-10-project-approval-dates) for JSON and flattened examples of the `milestones` building block.

#### I.12.3. Implementation milestones - Date of commissioning 

Contract Milestones (Estimated and Actual) - Date of commissioning

> The testing and inspection of the completed works to verify that the works are ready for commercial operation. ([Source](https://pppknowledgelab.org/glossary#Commissioning))

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

The milestone should have a `type` of 'delivery', a `code` of 'commissioning' and a status of either `scheduled` or `met` with either the date that this milestone was achieved in `dateMet`, or the scheduled date in `dueDate`.

**Example**: See [section I.10](#i-10-project-approval-dates) for JSON and flattened examples of the `milestones` building block.

#### I.12.4. Implementation milestones - Date of contract expiry 

Contract Milestones (Estimated and Actual) - Date of contract expiry

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

Information on the expected contract expiry date at the tender and award stages of a contracting process should be provided using `contractPeriod` field in the `tender` and `award` sections respectively.

This expected date of contract expiry should be entered into the `contractPeriod/endDate` field.

Information on the actual contract expiry date should be provided using the `period` field in the `contract` section.

The actual date of contract expiry should be entered into the `period/endDate` field.  

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [tender/contractPeriod](../reference/schema/#release-schema.json,,tender/contractPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: contractPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender/contractPeriod
  :ignore_path: /releases/1/
```

</div>

### I.13. Contract documents 

Links to all contract documents

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

Links to contract documents can be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array.  Each document's `documentType` field should be set to one of 'contractDraft', 'contractSigned' or 'contractSchedule'. (The contract may have a `status` of 'pending' up until it is signed.)

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### I.14. Contract parties - public authority 

Public authority: name of authority, name of representative, address, telephone, fax, e-mail

> The unit/body/department within a government that is tendering and contracting the project. The public counterpart in the PPP contract. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

#### I.14.1. Contract signatories 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

References to all signatories to the contract (including the public authority) should be provided using [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) objects in the [contracts/signatories](../reference/schema/#release-schema.json,,contracts/0/signatories) array, referencing the relevant entries in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/signatories
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/signatories
  :ignore_path: /releases/4/
```

</div>

#### I.14.2. Organization details 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

Details of the public authority, including name and contact details, should be provided using an [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) object in the [parties](../reference/schema/#release-schema.json,,parties) array. The party's `roles` array should include the 'publicAuthority' code, and the party's `contactPoint` field can be used to provide details of a named representative.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/parties/1
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/parties/1
  :ignore_path: /releases/0/
```

</div>

#### I.14.3. Organization reference 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

A reference to the public authority should be provided using an [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) object in the [publicAuthority](../reference/schema/#release-schema.json,,publicAuthority) field, referencing the relevant entry in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/0/publicAuthority
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/0/publicAuthority
  :ignore_path: /releases/0/
```

</div>

### I.15. Contract parties - private party 

Private party: name of company or consortium, name of representative, address, telephone, fax, e-mail

> The counter party of the procuring authority in the PPP contract. A private entity which has been granted the contract to construct and operate a government asset, and which is usually created under the form of a Special Purpose Vehicle or SPV. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

#### I.15.1. Contract signatories 

References to all signatories to the contract (including the private party) should be provided using [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) objects in the [contracts/signatories](../reference/schema/#release-schema.json,,contracts/0/signatories) array, referencing the relevant entries in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/signatories
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/signatories
  :ignore_path: /releases/4/
```

</div>

#### I.15.2. Organization details 

Details of the private party, including name and contact details, should be provided using an [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) object in the [parties](../reference/schema/#release-schema.json,,parties) array. The party's `roles` array should include the 'privateParty' code, and the party's `contactPoint` field can be used to provide details of a named representative.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/parties/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/parties/0
  :ignore_path: /releases/4/
```

</div>

#### I.15.3. Organization reference 

A reference to the private party should be provided using an [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) object in the [awards/preferredBidders](../reference/schema/#release-schema.json,,awards/0/preferredBidders) field, referencing the relevant entry in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/awards/0/preferredBidders
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/awards/0/preferredBidders
  :ignore_path: /releases/3/
```

</div>

### I.16. Contract parties - financiers 

Financiers: name of Lead FI, other FIs, name of representative of lead FI, address, telephone, fax, e-mail

#### I.16.1. Organization details 

Details of the financiers, including name and contact details, should be provided using [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) objects in the [parties](../reference/schema/#release-schema.json,,parties) array. Each party's `roles` array should include the 'leadBank' or 'lender' code, as appropriate, and each party's `contactPoint` field can be used to provide details of a named representative.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/parties/4
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/parties/4
  :ignore_path: /releases/4/
```

</div>

#### I.16.2. Contract signatories 

References to all signatories to the contract (including any financiers that are signatories) should be provided using [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) objects in the [contracts/signatories](../reference/schema/#release-schema.json,,contracts/0/signatories) array, referencing the relevant entries in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/signatories
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/signatories
  :ignore_path: /releases/4/
```

</div>

## II. Procurement Information 

Dates and summary details, links to all procurement documents, final feasibility study, including land acquisition, social, environmental, and rehabilitation related information, reports of independent procurement auditors (if any)

### II.1. Pre qualification 

> The act of testing prospective bidders to determine whether they meet the pass/fail qualification criteria in advance of issuing the request for proposals. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

#### II.1.1. Dates - Submission period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

The `preQualification/period` field should be used to provide the period during which the pre-qualification stage is open for submissions, `period/endDate` should contain the closing date for submissions. 

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [preQualification/period](../reference/schema/#release-schema.json,,preQualification/period) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/7/preQualification/period
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/7/preQualification/period
  :ignore_path: /releases/7/
```

</div>

#### II.1.2. Dates - Enquiry period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

The `preQualification/enquiryPeriod` field should be used to provide the period during which enquiries may be made and answered. 

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [preQualification/enquiryPeriod](../reference/schema/#release-schema.json,,preQualification/enquiryPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/7/preQualification/enquiryPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/7/preQualification/enquiryPeriod
  :ignore_path: /releases/7/
```

</div>

#### II.1.3. Dates - Qualification period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

The `preQualification/qualificationPeriod` field should be used to provide the period during which candidates will be qualified or pre-selected (shortlisted).  

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [preQualification/qualificationPeriod](../reference/schema/#release-schema.json,,preQualification/qualificationPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/7/preQualification/qualificationPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/7/preQualification/qualificationPeriod
  :ignore_path: /releases/7/
```

</div>

#### II.1.4. Summary details - Submission method 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

Information on the submission method for bids should be provided in the `preQualification` section: 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: preQualification/submissionMethod,preQualification/submissionMethodDetails
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/7/preQualification
  :include_only: submissionMethod, submissionMethodDetails
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/7/preQualification
  :include_only: submissionMethod, submissionMethodDetails
  :ignore_path: /releases/7/
```

</div>

#### II.1.5. Summary details - Eligibility criteria 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

Information on the eligibility criteria for participants in the pre-qualification stage can be provided using `preQualification` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: preQualification/eligibilityCriteria
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/7/preQualification
  :include_only: eligibilityCriteria
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/7/preQualification
  :include_only: eligibilityCriteria
  :ignore_path: /releases/7/
```

</div>

#### II.1.6. RFQ documents 

RFQ documents

> The set of documents issued by the procuring authority that constitute the basis of the qualification and potentially the pre-selection of candidates (the short list). Qualified (or short-listed candidates) will then be invited to submit a proposal (or to enter into a new phase prior to bid submission, such as a dialogue phase or interactive phase). ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

Links to these documents should be provided using [Document](reference/documents) objects in the [preQualification/documents](../reference/schema/#release-schema.json,,preQualification/documents) array. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### II.2. List of pre-qualified suppliers 

Pre-qualification or shortlist

Details of the bidders should be provided using [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) objects in the [parties](../reference/schema/#release-schema.json,,parties) array.

* If the bidder is shortlisted or invited to submit a proposal following the pre-qualification process, the party's `roles` array should include the 'qualifiedBidder' code. 
* If the bidder is **neither** shortlisted **nor** invited to submit a proposal following the pre-qualification process, the party's `roles` array should include the 'disqualifiedBidder' code.

**Example**: See [section I.14.2](#i-14-2-organization-details) for JSON and flattened examples of the `organization` building block.

### II.3. Tender 

> The process by which bids are invited from interested parties to carry out the project. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

#### II.3.1. Dates - Tender period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

The `tender/tenderPeriod` field should be used to provide the period during which the tender is open for submissions, `tenderPeriod/endDate` should contain the closing date for tender submissions. 

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [tender/tenderPeriod](../reference/schema/#release-schema.json,,tender/tenderPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender/tenderPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender/tenderPeriod
  :ignore_path: /releases/1/
```

</div>

#### II.3.2. Dates - Enquiry period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

The `tender/enquiryPeriod`field should be used to provide the period during which enquiries may be made and answered. 

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [tender/enquiryPeriod](../reference/schema/#release-schema.json,,tender/enquiryPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender/enquiryPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender/enquiryPeriod
  :ignore_path: /releases/1/
```

</div>

Some PPP procurement processes have more than one enquiry period during the tender stage of the procurement. In such cases:

* The `tender/enquiryPeriod` field should be used to provide the **next** period during which enquiries may be made and answered, if there are no further enquiry periods scheduled the field should be used to provide the **most recent** period during which enquiries may be made and answered. Where an OCDS release is published during an enquiry period the `tender/enquiryPeriod` field should be used to provide the start and end dates of the **current** enquiry period.
* The `tender/milestones` block should be used to provide details of any subsequent enquiry periods beyond the next period during which enquiries may be made and answered.

The above guidance should also be followed for processes with multiple enquiry periods during the pre-qualification stage of the procurement, in such cases the same approach should be applied to the equivalent fields from the `preQualification` section. 

#### II.3.3. Dates - Award period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

The `tender/awardPeriod` field should be used to provide the period during which an award is expected to be made. 

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [tender/awardPeriod](../reference/schema/#release-schema.json,,tender/awardPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender/awardPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender/awardPeriod
  :ignore_path: /releases/1/
```

</div>

#### II.3.4. Dates - Contract period 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U   U   U   U   U 
==  ==  ==  ==  ==  ==

```

</div>

The `tender/contractPeriod` field should be used to provide the expected start and end dates for the contract. 

**Schema**: Information can be provided using a [Period](https://standard.open-contracting.org/1.1/en/schema/reference/#period) object in the [tender/contractPeriod](../reference/schema/#release-schema.json,,tender/contractPeriod) field.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: contractPeriod
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender/contractPeriod
  :ignore_path: /releases/1/
```

</div>

#### II.3.5. Summary details - Procurement method 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

Information on the procurement method used should be provided in the `tender` section: 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: tender/procurementMethod,tender/procurementMethodDetails,tender/procurementMethodRationale
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: procurementMethod, procurementMethodDetails, procurementMethodRationale
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: procurementMethod, procurementMethodDetails, procurementMethodRationale
  :ignore_path: /releases/1/
```

</div>

#### II.3.6. Summary details - Submission method 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

Information on the submission method for bids should be provided in the `tender` section: 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: tender/submissionMethod,tender/submissionMethodDetails
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: submissionMethod, submissionMethodDetails
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: submissionMethod, submissionMethodDetails
  :ignore_path: /releases/1/
```

</div>

#### II.3.7. Summary details - Eligibility criteria 

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

Information on the eligibility criteria for bidders can be provided using `tender` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: tender/eligibilityCriteria
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: eligibilityCriteria
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/1/tender
  :include_only: eligibilityCriteria
  :ignore_path: /releases/1/
```

</div>

#### II.3.9. Other documents

<div class="disclosure-timing">

```eval_rst
==  ==  ==  ==  ==  ==
PP  P   A   CC  I   R 
==  ==  ==  ==  ==  ==
P   U                 
==  ==  ==  ==  ==  ==

```

</div>

Links to procurement documents, feasibility studies, including land acquisition, social, environmental, and rehabilitation related information and reports of independent procurement auditors should be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### II.4. Evaluation criteria 

Evaluation criteria: brief description with weightage

Links to these documents should be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'evaluationCriteria'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### II.5. Evaluation committee information 

Brief information on constitution of the evaluation committees

Links to these documents can be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'evaluationCommittee'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### II.6. Negotiation parameters 

Negotiation parameters: brief description of the parameters for negotiation with preferred proponent

Links to these documents can be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'negotiationParameters'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### II.7. Pre-bid meeting minutes 

Minutes of pre-bid meetings

Links to these documents can be provided using [Document](reference/documents) objects in the [tender/documents](../reference/schema/#release-schema.json,,tender/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'minutes'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### II.8. Contract award 

#### II.8.1. Organization details 

Details of the preferred bidder, including name and contact details, should be provided using an [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) object in the [parties](../reference/schema/#release-schema.json,,parties) array. The party's `roles` array should include the 'preferredBidder' code, and the party's `contactPoint` field can be used to provide details of a named representative.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/parties/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/parties/0
  :ignore_path: /releases/3/
```

</div>

#### II.8.2. Organization reference 

A reference to the preferred bidder should be provided using an [OrganizationReference](https://standard.open-contracting.org/1.1/en/schema/reference/#organizationreference) object in the [awards/preferredBidders](../reference/schema/#release-schema.json,,awards/0/preferredBidders) field, referencing the relevant entry in the `parties` section.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/awards/0/preferredBidders
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/awards/0/preferredBidders
  :ignore_path: /releases/3/
```

</div>

## III. Risk 

### III.1. Individual risk allocation information 

Listing of risks with information on who bears the risk. Countries, sectors, and individual projects may use different categorizations. Several risks can be further broken down into components or listed together. If within a large category of risk subcategories are allocated to different parties, it makes sense to show the subcategories clearly.

> The allocation of the consequences of each risk to one of the parties in the contract, or agreeing to deal with the risk through a specified mechanism which may involve sharing the risk. ([Source](https://ppp-certification.com/ppp-certification-guide/glossary))

#### III.1.1. Structured risk allocation information 

Structured information on the risk allocation should be provided using the `contract/riskAllocation` section.

The following information should be provided for each risk:

* Risk category
* Description
* Allocation

Additional free text information on each risk allocation, for example the rationale for the allocation, can also be provided.

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/riskAllocation
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/riskAllocation
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/riskAllocation
  :ignore_path: /releases/4/
```

</div>

#### III.1.2. Additional financial modelling for risks 

Links to these documents can be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. Each document's `documentType` field should be set to 'riskProvisions'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

## IV. Evaluation of PPP option 

### IV.1. Evaluation report 

Link to evaluation report (value for money or other)

Links to these documents can be provided using [Document](reference/documents) objects in the [awards/documents](../reference/schema/#release-schema.json,,awards/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'evaluationReports'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### IV.2. Summary data 

#### IV.2.1. Rationale for project as PPP (specific) 

State the rationale for doing the project as a PPP, including any qualitative or quantitative value-for-money or other analysis that might have been used. If nonfinancial benefits have been quantified or considered, these could be stated

*Note: Choice of methodology affects the costs to the public and it is important to assure them that the PPP mode selected is the best possible in terms of cost, given equal standards of service in all modes tested.*

Links to these documents can be provided using [Document](reference/documents) objects in the [awards/documents](../reference/schema/#release-schema.json,,awards/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'valueForMoneyAnalysis'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

##### IV.2.2.1. Discount rate and risk premium - structured data

The discount rates used should be specified in the disclosure along with the risk premium used, if any, and an explanation for the rate of risk premium used, referring to guidance, if any available in this regard or describing project-specific circumstances that justify the risk premium rate used.

Structured information and supporting details about the discount rate and risk premium used by government to evaluate the PPP should be provided in the `award/evaluationIndicators` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: awards/0/evaluationIndicators
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/awards/0/evaluationIndicators
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/awards/0/evaluationIndicators
  :ignore_path: /releases/3/
```

</div>

##### IV.2.2.2. Discount rate and risk premium - supporting documentation 

Links to supporting documentation about the discount rate and risk premium used by government to evaluate the PPP can be provided using [Document](reference/documents) objects in the [awards/documents](../reference/schema/#release-schema.json,,awards/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'discountRate'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### IV.2.3. Risk comparison 

Risk comparison of other financing mechanisms should be specified.

Links to these documents can be provided using [Document](reference/documents) objects in the [awards/documents](../reference/schema/#release-schema.json,,awards/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'riskComparison'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

## V. Financial Information 

### V.1. Debt-equity ratio 

Debt-equity ratio

Structured information and supporting details about the debt-equity ratio for the PPP should be provided in the `contract/financeSummary` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/financeSummary
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: debtEquityRatio, debtEquityRatioDetails
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: debtEquityRatio, debtEquityRatioDetails
  :ignore_path: /releases/4/
```

</div>

### V.2. Share capital 

Share capital

Structured information and supporting details about the share capital of the PPP should be provided in the `contract/financeSummary` section. 

**Schema**: See above

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: shareCapital, shareCapitalDetails
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: shareCapital, shareCapitalDetails
  :ignore_path: /releases/4/
```

</div>

### V.3. Shareholders with proportion held and voting rights 

Shareholders with proportion held and voting rights

#### V.3.1. Shareholder organization details 

Details of the shareholders should be provided using [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) objects in the [parties](../reference/schema/#release-schema.json,,parties) array. Each party's `roles` array should include the 'equityInvestor' code.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/parties/4
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/parties/4
  :ignore_path: /releases/3/
```

</div>

#### V.3.1. Proportion held and voting rights 

Structured information about each shareholder on the proportion of shares held and voting rights should be provided in the entry in the `parties/shareholders` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: parties/0/shareholders
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/parties/0/shareholders
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/parties/0/shareholders
  :ignore_path: /releases/3/
```

</div>

### V.4. Equity transfer caps 

Equity transfer caps

*Note: Certain contracts provide for caps on equity transfer in different stages of the contract, especially during the construction stage and for a few years thereafter. Give details of any such provisions.*

#### V.4.1. Documentation of equity transfer caps 

Links to these documents can be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'equityTransferCaps'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### V.4.2. Individual shareholder lock in arrangements 

Information on equity transfer caps or lock in arrangements applicable to a particular shareholder can be provided in the `parties/shareholders/notes` field. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: parties/0/shareholders/0/notes
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/3/parties/0/shareholders/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/3/parties/0/shareholders/0
  :ignore_path: /releases/3/
```

</div>

### V.5. Lender and investor information 

Commercial lenders, institutional investors, bilateral or multilateral lenders, public issue of bonds, supplier credit, other

#### V.5.1. Organization information 

Details of the lenders and investors should be provided using [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) objects in the [parties](../reference/schema/#release-schema.json,,parties) array. Each party's `roles` array should include the 'lender' or 'equityInvestor' code, as appropriate.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/parties/4
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/parties/4
  :ignore_path: /releases/4/
```

</div>

#### V.5.2. Financing information 

Details of the type of finance provided by each lender or investor should be provided in the `contract/finance` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/finance
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0
  :ignore_path: /releases/4/
```

</div>

### V.6. Debt information 

Categorize senior debit, mezzanine debit, other

Details of all debt financing should be provided in the `contract/finance` section.

*Note: Not all fields are required or applicable to all types of financing arrangement.* 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/finance/0/financeType,contracts/0/finance/0/financeCategory
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0
  :include_only: financeType, financeCategory
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0
  :include_only: financeType, financeCategory
  :ignore_path: /releases/4/
```

</div>

### V.7. Rate information 

Amount and tenor of each, fixed or floating rate

Details of interest rates relating to each finance arrangement should be provided in the `contract/finance` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/finance/0/interestRate
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0/interestRate
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0/interestRate
  :ignore_path: /releases/4/
```

</div>

### V.8. Security information 

Security and step in arrangements

#### V.8.1. Structured security and step in information 

Details of security and step in rights relating to each financing arrangement should be provided in the `contract/finance/description` field, whilst the `contract/finance/stepInRights` flag should be set for each financing arrangement to indicate whether step in rights apply. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/finance/0/description,contracts/0/finance/0/stepInRights
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0
  :include_only: description, stepInRights
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/finance/0
  :include_only: description, stepInRights
  :ignore_path: /releases/4/
```

</div>

#### V.8.2. Security and step in documentation 

Links to these documents can be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'financeArrangements'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### V.9. Forecast IRR 

Forecast IRR

Structured information and supporting details about the forecast IRR of the PPP should be provided in the `contract/financeSummary` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/financeSummary
    :collapse: contracts/0/financeSummary/projectIRR,contracts/0/financeSummary/projectIRRDetails
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: projectIRR, projectIRRDetails
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: projectIRR, projectIRRDetails
  :ignore_path: /releases/4/
```

</div>

## VI. Government Support 

### VI.1. Guarantee information 

Detail the type and exact details of the guarantees provided - both explicit and contingent guarantees - such as minimum revenue guarantee, exchange rate guarantee, debit repayment guarantee and other guarantees. Provide links to fiscal commitments and contingent liabilities disclosure reports, if any.

#### VI.1.1. Structured information on guarantees 

Structured information about financial guarantees can be provided in the contract `finance` block, with a `financeCategory` code of 'guarantee'. This allows information about the party providing the guarantee, the total value, and any period it covers, to be represented. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/finance
    :collapse: contracts/0/finance/0/interestRate,contracts/0/finance/0/repaymentFrequency
    :nocrossref:
```

#### VI.1.2. Guarantee documentation 

Links to documentation or reports on each guarantee should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'guarantee'.

### VI.2. Grant/Subsidy information 

#### VI.2.1. Subsidy as a proportion of project value 

Subsidy as a proportion of project value

#### VI.2.1. Structured information on subsidy as a proportion of project value 

Structured information and supporting details about the subsidy ratio for the PPP should be provided in the `contract/financeSummary` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/financeSummary/subsidyRatio,contracts/0/financeSummary/subsidyRatioDetails
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: subsidyRatio, subsidyRatioDetails
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/financeSummary
  :include_only: subsidyRatio, subsidyRatioDetails
  :ignore_path: /releases/4/
```

</div>

#### VI.2.1. Supporting documentation on subsidy as a proportion of project value 

Links to these documents can be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'grants'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### VI.2.2. Supporting documentation on capital subsidies 

Capital subsidies paid during construction with periodicity of milestones

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'grants'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### VI.2.3. Supporting documentation on operating subsidies 

Operating subsidies and their periodicity of milestones

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VI.3. Service payment information 

These are payments made by the public authority or purchaser to the private provider for infrastructure services (applicable in PFI type projects)

#### VI.3.1. Structured information on individual service payments 

Structured information on actual individual service payments can be provided in the `contract/implementation/transactions` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/implementation/transactions
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/5/contracts/0/implementation/transactions/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/5/contracts/0/implementation/transactions/0
  :ignore_path: /releases/5/
```

</div>

#### VI.3.2. Structured information on total service payments 

Total payments and periodicity

Structured information on total service payments can be provided in the `contract/implementation/charges` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/implementation/charges
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/implementation/charges
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/implementation/charges
  :ignore_path: /releases/4/
```

</div>

#### VI.3.3. Service payment calculation methodology 

Methodology for calculating payments

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'servicePayments'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### VI.3.4. Service payment indexation 

Indexation used

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'servicePayments'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VI.4. Land leases, asset transfers information 

* Land transferred on lease or other basis by government: give details of property numbers with the quantum of land transferred, zoning information, conditions of transfer
* Equipment transfers: details of equipment with conditions of transfer
* Human resources/personnel transfers: details and conditions of transfer

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'lease' or 'assetTransfer'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VI.5. Other support 

* Non-complete clauses
* Provision for revenue shortfall loan

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'otherGovernmentSupport'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VI.6. Revenue share information 

* Revenue share on base case
* Revenue share on upside
* Links to graphs: annual concessionaire payments to government

#### VI.6.1. Revenue share agreed in contract 

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'revenueShare'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### VI.6.2. Revenue share in operation during contract 

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/implementation/documents](../reference/schema/#release-schema.json,,contracts/0/implementation/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'revenueShare'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

## VII. Tariffs 

### VII.1. Tariffs and pricing 

Tariffs and pricing

This information will be required only where the infrastructure is financed partly or fully through the levy of user charges

Structured information on the tariffs defined in the contract and subsequent revisions to tariffs can be provided in the implementation section using the tariffs extension. Tariffs and pricing schedules can also be provided as documents. 

#### VII.1.1. Structured tariff and pricing information 

Structured information on the tariffs defined in the contract should be provided in the `contract/tariffs` section and subsequent revisions to tariffs can be provided in the `implementation/tariffs` section. 

Information on who pays the tariff can be modelled using a `dimension` in cases where different charges apply to different parties. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/implementation/tariffs
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/implementation/tariffs
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/4/contracts/0/implementation/tariffs
  :ignore_path: /releases/4/
```

</div>

#### VII.1.2. Tariff and pricing documentation 

Tariffs and pricing schedules defined in the contract can be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'tariffs'.

Subsequent revisions to tariffs and pricing schedules can similarly be provided using [Document](reference/documents) objects in the [contracts/implementation/documents](../reference/schema/#release-schema.json,,contracts/0/implementation/documents) array.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VII.2. Tariff setting methodology 

Methodology for tariff setting/pricing

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'tariffMethod'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VII.3. Tariff review mechanism 

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VII.4. Tariff change illustrations 

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to 'tariffIllustration'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

## VIII. Contract Termination 

### VIII.1. Events of default and termination payments 

Describe key events of default under two major categories: concessionaires events of default and public authority's events of default. State the termination payments against each, stating clearly the methodology used for total payments. The following format may be used:

Provision for contract termination should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document should be provided using its `description` field. Each document's `documentType` field should be set to 'termination'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### VIII.2. Handover information 

State details of hand over of assets back to state, condition of assets, and any other conditions relating to hand over. Include details of provision for continuity of service

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document should be provided using its `description` field. Each document's `documentType` field should be set to 'handover'.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

## IX. Renegotiations 

### IX.1. Contract variation details 

State variations to contract, if any, after signing of the original contract detailing each change against original provisions. State in addition the details of renegotiations and circumstances leading to renegotiations. State specifically any change due to the renegotiated clauses in the following: roles and responsibilities relating to the project, risk allocation, fiscal exposure, that is, any change in fiscal commitments and contingent liabilities with a rationale for agreeing to the change.

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/8/contracts/0/amendments/0
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/8/contracts/0/amendments/0
  :ignore_path: /releases/8/
```

</div>

#### IX.1.1. Contract documents 

The amended contract should be provided using a [Document](reference/documents) object in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of the **variations to the contract** should be provided using the document's `description` field. The document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

#### IX.1.2. Description 

Nature of Variation

A description of the nature of the variation should be provided in the `amendment/description` field. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/amendments/0/description
    :collapse: 
    :nocrossref:
```

#### IX.1.3. Rationale 

Rationale for variation

A rationale for the variation should be provided in the `amendment/rationale` field. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/amendments/0/rationale
    :collapse: 
    :nocrossref:
```

#### IX.1.4. Parties 

Change in roles and responsibilities of the parties due to the variation, if any

Structured information on changes to the roles and responsibilities of the parties due to the variation should be provided by updating the relevant [Organization](https://standard.open-contracting.org/1.1/en/schema/reference/#parties) objects in the [parties](../reference/schema/#release-schema.json,,parties) array.

#### IX.1.5. Risk allocation 

Change in original risk allocation due to the variation, if any

Structured information on changes to the original risk allocation due to the variation should be provided by updating the `contract/riskAllocation` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/riskAllocation
    :collapse: 
    :nocrossref:
```

#### IX.1.6. Fiscal commitments 

Change in original fiscal commitments or contingent liabilities of government due to the variation, if any

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document should be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### IX.1.6. Costs 

Change in capital or operational costs due to the variation, if any

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/documents](../reference/schema/#release-schema.json,,contracts/0/documents) array. A short summary of each document should be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

#### IX.1.7. Tariffs 

Change in tariffs or service levels due to the variation, if any

Structured information on changes to the tariffs should be provided by updating the `contract/implementation/tariffs` section. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/implementation/tariffs
    :collapse: 
    :nocrossref:
```

#### IX.1.8. Service levels 

Structured information on changes to services levels should be provided by updating the [Metric](https://extensions.open-contracting.org/en/extensions/metrics/master/schema/#metric) objects in the [contracts/agreedMetrics](../reference/schema/#release-schema.json,,contracts/0/agreedMetrics) array.

#### IX.1.9. Date 

Date of variation

The date of the variation should be provided using the `amendment/date` field. 

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/amendments/0/date
    :collapse: 
    :nocrossref:
```

## X. Performance Information 

### X.1. Actual annual demand 

State the actual annual measured levels of demand or stated levels of demand in the providers report or contract managers report. Use the following format

Structured data about estimated demand should be provided using [Metric](https://extensions.open-contracting.org/en/extensions/metrics/master/schema/#metric) objects in the [contracts/implementation/metrics](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics) array.

A metric with an `id` of 'demand' should be given, with a series of [observations](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations) that capture the actual demand for a given period. These estimates can be disaggregated by any number of dimensions contained as key-value pairs within each observation's [dimensions](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations/0/dimensions) object. 

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/6/contracts/0/implementation/metrics
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/6/contracts/0/implementation/metrics
  :ignore_path: /releases/6/
```

</div>

### X.2. Actual annual revenue 

Recommended only where revenue share clauses or other related clauses such as MRGs are present in the contract.

#### X.2.1. Structured information on annual revenues 

State the actual annual total revenues reported in the financial statements and reports.

Structured data about aggregated annual revenues can be provided using [Metric](https://extensions.open-contracting.org/en/extensions/metrics/master/schema/#metric) objects in the [contracts/implementation/metrics](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics) array.

A metric with an `id` of 'revenue' should be given, with a series of [observations](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations) that capture the actual revenue for a given period. These estimates can be disaggregated by any number of dimensions contained as key-value pairs within each observation's [dimensions](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations/0/dimensions) object. 

**Example**: See [section X.1](#x-1-actual-annual-demand) for JSON and flattened examples of the `metrics` building block.

#### X.2.2. Financial statements 

Provide links to audited financial statements of the provider company.

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/implementation/documents](../reference/schema/#release-schema.json,,contracts/0/implementation/documents) array. A short summary of each document can be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

### X.3. Actual IRR 

Recommended only where there is government equity investment or other form of government support that is substantial

Structured data about actual IRR can be provided using [Metric](https://extensions.open-contracting.org/en/extensions/metrics/master/schema/#metric) objects in the [contracts/implementation/metrics](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics) array.

A metric with an `id` of 'IRR' should be given, with a series of [observations](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations) that capture the actual revenue for a given period. These estimates can be disaggregated by any number of dimensions contained as key-value pairs within each observation's [dimensions](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations/0/dimensions) object. 

**Example**: See [section X.1](#x-1-actual-annual-demand) for JSON and flattened examples of the `metrics` building block.

### X.4. Actual KPI performance 

State actual year-wise performance here against each of 10-12 identified key performance indicators

Structured data about actual performance against KPIs can be provided using [Metric](https://extensions.open-contracting.org/en/extensions/metrics/master/schema/#metric) objects in the [contracts/implementation/metrics](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics) array.

These estimates can be disaggregated by any number of dimensions contained as key-value pairs within each observation's [dimensions](../reference/schema/#release-schema.json,,contracts/0/implementation/metrics/0/observations/0/dimensions) object. 

**Example**: See [section X.1](#x-1-actual-annual-demand) for JSON and flattened examples of the `metrics` building block.

### X.5. Performance failure information 

State instances of performance failure during the year and the penalty or abatement. Provide information on the provision of the contract as well as the actual penalties imposed.

Structured data about actual performance failures, penalties and abatements and those provided for in the contract can be provided in the `contract/implementation/performanceFailures` section.

**Schema**: Information can be provided using the following OCDS fields.

```eval_rst
.. jsonschema:: _static/patched/release-schema.json
    :include: contracts/0/implementation/performanceFailures
    :collapse: 
    :nocrossref:
```

**JSON example:**

```eval_rst
.. jsoninclude:: examples/full.json
  :jsonpointer: /releases/6/contracts/0/implementation/performanceFailures
  
```

**Flattened example** (showing top-level fields only)

<div class="flattened-example">

```eval_rst
.. jsoninclude-flat:: examples/full.json
  :jsonpointer: /releases/6/contracts/0/implementation/performanceFailures
  :ignore_path: /releases/6/
```

</div>

### X.6. Performance assessment reports 

Provide links to audit report, independent performance assessments of the the independent engineer and any other performance reports available for the project.

Links to these documents should be provided using [Document](reference/documents) objects in the [contracts/implementation/documents](../reference/schema/#release-schema.json,,contracts/0/implementation/documents) array. A short summary of each document should be provided using its `description` field. Each document's `documentType` field should be set to a value from the [document type codelist](../reference/codelists/#documenttype), to identify the type of document being disclosed.

**Example**: See [section I.4](#i-4-project-economic-and-social-benefits) for JSON and flattened examples of the `documents` building block.

