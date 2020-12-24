# Changelog

## Iterative improvements

* [#230](https://github.com/open-contracting-extensions/public-private-partnerships/pull/230) Reduce the degree of repetition on the Frameworks reference page.
* [#231](https://github.com/open-contracting-extensions/public-private-partnerships/pull/231) Add a link to the release schema as a CSV spreadsheet.

## [1.0.0.beta2] - 2019-10-21

### Normative changes

* [#203](https://github.com/open-contracting-extensions/public-private-partnerships/pull/203) The profile has been upgraded to OCDS 1.1.4. All core extensions have been upgraded to v1.1.4: Bid statistics and details, Location, Milestone documents, Process level title and description. All community extensions have been upgraded to their latest versions.
* [#205](https://github.com/open-contracting-extensions/public-private-partnerships/pull/205) The documentType codelist has been updated:
  * 'contractSchedules' has been renamed to 'contractMilestones'.
  * The description of 'needsAssessment' has been updated to match the description from OC4IDS.
  * The description of 'environmentalImpact' has been updated to match the description from OC4IDS.

### Non-normative changes

* [#223](https://github.com/open-contracting-extensions/public-private-partnerships/pull/223) In the descriptions of fields in the profile's release schema, link to the profile's codelists documentation page, instead of OCDS' codelists documentation page, if the codelist is modified by the profile.
* [#222](https://github.com/open-contracting-extensions/public-private-partnerships/pull/222) Clarify the one-to-one correspondence between a PPP project and a contracting process.
* [#195](https://github.com/open-contracting-extensions/public-private-partnerships/pull/195) The documentation pages of all extensions have been moved to the new [Extension Explorer](https://extensions.open-contracting.org/).
* [#206](https://github.com/open-contracting-extensions/public-private-partnerships/pull/206) Links to the milestones extension documentation have been replaced with links to the standard documentation.
* [#212](https://github.com/open-contracting-extensions/public-private-partnerships/pull/212) The codelist reference page has been updated to:
  * Separate out codelists from OCDS which are reused without modification and those which are modified.
  * Add codelists which were present in the profile but missing from the documentation.
  * Add links to additional codelist documentation in the OCDS documentation and the Extension Explorer.
* [#214](https://github.com/open-contracting-extensions/public-private-partnerships/pull/214) Replace mentions of 'OCDS core' with 'OCDS'.
* [#209](https://github.com/open-contracting-extensions/public-private-partnerships/pull/209) A schema browser has been added.
* [#210](https://github.com/open-contracting-extensions/public-private-partnerships/pull/10) This changelog has been added.
* The build process for the documentation has been improved ([#182](https://github.com/open-contracting-extensions/public-private-partnerships/pull/182), [#183](https://github.com/open-contracting-extensions/public-private-partnerships/pull/183), [#184](https://github.com/open-contracting-extensions/public-private-partnerships/pull/184), [#185](https://github.com/open-contracting-extensions/public-private-partnerships/pull/185), [#190](https://github.com/open-contracting-extensions/public-private-partnerships/pull/190), [#219](https://github.com/open-contracting-extensions/public-private-partnerships/pull/219), [#220](https://github.com/open-contracting-extensions/public-private-partnerships/pull/220), [#220](https://github.com/open-contracting-extensions/public-private-partnerships/pull/221)).

### Fixes

* [#202](https://github.com/open-contracting-extensions/public-private-partnerships/pull/202), [#203](https://github.com/open-contracting-extensions/public-private-partnerships/pull/203), [#204](https://github.com/open-contracting-extensions/public-private-partnerships/pull/204) The worked example JSON files have been updated:
  * Remove the `planning.budget.amount` field which is not referenced in the framework reference.
  * Remove trailing '.0' from strings comprised entirely of numeric characters.
  * Fix unresolvable organization references for shareholders.
  * Correct incorrect use of the `identifier.uri` field.

## [1.0.0.beta] - 2018-08-16

This changelog entry indicates notable changes since the initial release of OCDS for PPPs. It is not intended to be a complete list of changes.

In addition to the specific changes below:

* [#121](https://github.com/open-contracting-extensions/public-private-partnerships/pull/121) Various fixes to codelist files (unquoted line breaks, blank rows, etc.)
* [#121](https://github.com/open-contracting-extensions/public-private-partnerships/pull/121) Various fixes to broken links, typos, grammar and capitalization in the documentation, schema and codelists.

### Normative changes

* [#121](https://github.com/open-contracting-extensions/public-private-partnerships/pull/121) The core extensions were upgraded to v1.1.3.
* [#133](https://github.com/open-contracting-extensions/public-private-partnerships/pull/133) Descriptions were added for the 'financeArrangements' and 'guaranteeReports' codes in the documentType codelist.

### Non-normative changes

* [#164](https://github.com/open-contracting-extensions/public-private-partnerships/pull/164) A patched release package schema is now distributed with the profile.
* [#121](https://github.com/open-contracting-extensions/public-private-partnerships/pull/121) The build process for the documentation was aligned with the common profile build process.

### Fixes

* [#121](https://github.com/open-contracting-extensions/public-private-partnerships/pull/121) `tag` `enum` updated to reflect changes to the `releaseTag` codelist.
* [#136](https://github.com/open-contracting-extensions/public-private-partnerships/pull/136) Set `uniqueItems` and `wholeListMerge` to `true` for `planning.project.additionalClassifications` and `planning.project.locations`.
