# Overview

```eval_rst
.. image:: _static/images/documents_data_presentation.png
   :align: right
```

The [World Bank PPP Disclosure Framework](http://www.worldbank.org/en/topic/publicprivatepartnerships/brief/ppp-tools#T1) sets out **what** should be disclosed as part of a Public Private Partnership process.

OCDS for PPPs provides a framework for **how** to publish the requested information, with clear separation of:

* Data
* Documents
* Presentation

The [OCDS releases and records model](http://standard.open-contracting.org/latest/en/getting_started/releases_and_records/) is designed to support **real time** updates, with data and documents on each stage of a process published and updated on an ongoing basis. 

## Data

```eval_rst
.. image:: _static/images/structured_shareholding.png
   :align: right
   :width: 400
   :target: ../spreadsheet/index.html
```

Many elements of the PPP framework call for **structured data**. For example:

* Project values over time;
* A breakdown of the project budget;
* Project metrics and delivery;
* Details of project finance;
* A list of shareholders, and shares held;

OCDS for PPPs provides structured data elements to represent this information, using existing OCDS building blocks, or [selected extensions](extensions). 

These structured data elements can be represented using JSON data, or via simple spreadsheet templates. 

## Documents

PPP projects involve can involve 100s or 1000s of pages of documents. 

The framework calls for:

* Disclosure of key documents;
* Presentation of summary information for easy public consumption;

Use OCDS to:

* Provide summary text for each framework element;
* Link directly to the page in attached documents where more information can be found **or** describe where documents can be accessed;

This way, stakeholders can more easily find the information they need to understand a project: and compliance with the framework can be more easily assessed. 

```eval_rst
.. note:: Make sure that documents are directly accessible at a persistent web address. Avoid placing documents behind a log-in or CAPTCHA, or moving the location of documents once they have been published.

```

## Presentation 

```eval_rst
.. image:: _static/images/ocds_show.png
   :align: right
   :width: 400
   :target: https://open-contracting.github.io/ocds-show-ppp/?load=https://raw.githubusercontent.com/open-contracting/ocds-show-ppp/master/example/full.json
```

With the combination of:

* Structured data;
* Online documents;

It is possible to build custom interfaces onto PPP disclosures: tailored to different audiences.

In particular:

* OCDS Show is a prototype interface that can be used to browse all the information in OCDS for PPPs releases and records; 
* OCDS for PPP data can be converted into spreadsheet formats for detailed analysis;
* Any third-party can build an interface using the OCDS for PPPs standard;

You can explore a [preview of OCDS Show with example data](https://open-contracting.github.io/ocds-show-ppp/?load=https://raw.githubusercontent.com/open-contracting/ocds-show-ppp/master/example/full.json).
