# Worked Example

OCDS for PPPs can be used to build up a clear record of all the stages of a Public Private Partnership project over time.

Fully implemented, it will bring together, in a structured form, key documents and data.

This allows different stakeholders to understand how a project has developed.

## Details

```eval_rst
.. image:: _static/images/ocds_show.png
   :target: https://open-contracting.github.io/ocds-show-ppp/?load=https://raw.githubusercontent.com/open-contracting/ocds-show-ppp/master/example/full.json
```

Based on our pilot work with the Red Compartida programme, we have created a fictional example PPP.

We used the [spreadsheet template](spreadsheet.md) to prepare a series of releases of data, representing different stages of the procurement process.

This was exported as an Excel file, and converted into JSON using the [OCDS Data Review Tool](https://standard.open-contracting.org/review/)

The releases were then compiled into a record, and are available to browse using [OCDS Show](https://github.com/open-contracting/ocds-show-ppp), an open source tool which provides:

* A templating engine for displaying OCDS releases and records;
* Alerts to changed fields between different releases;
* Example visualization of data;

## Explore the example

View the [OCDS releases in JSON format here](../_static/full.json).

View the [OCDS record in JSON format here](../_static/full_record_package.json).

View the [data in OCDS show here](https://open-contracting.github.io/ocds-show-ppp/?load=https://raw.githubusercontent.com/open-contracting/ocds-show-ppp/master/example/full_record_package.json).

In the record within OCDS show:

* The circles along the top represent new 'releases' of information;
* The sections down to side reflect stages of the contracting process;
* The record 'builds up' as information is provided, and highlights what has changed at each point;

Use the 'text input' button to see (and adapt) the JSON data which generates this view.

Use a web browser add-on for a more user friendly preview of the JSON files. You can install [JSONView for Chrome](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc), [JSONView for Firefox](https://addons.mozilla.org/en-us/firefox/addon/jsonview/) or [JSONView for Safari](https://safari-extensions.apple.com/details/?id=com.dcrousso.jsonview-safari-Q5M4T22BE9)

Alternative presentations of data can be prepared using the open source [OCDS Show](https://github.com/open-contracting/ocds-show-ppp) tool.
