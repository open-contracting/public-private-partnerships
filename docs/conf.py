#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 20 21:53:17 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import re
from glob import glob
from pathlib import Path

import standard_theme
from ocds_babel.translate import translate
from recommonmark.transform import AutoStructify

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinxcontrib.jsonschema',
    'sphinxcontrib.opencontracting',
    'sphinxcontrib.opendataservices',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Open Contracting Data Standard for Public Private Partnerships'
copyright = 'Open Contracting Partnership'
author = 'Open Data Services / Open Contracting Partnership'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0-beta2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'standard_theme'
html_theme_path = [standard_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'examples']


# -- Local configuration --------------------------------------------------

def update_codelist_urls(text, codelists):
    def replace(match):
        codelist = match.group(2).replace('-', '')
        if any(name for name in codelists if name.lower()[:-4] == codelist):
            return match.group(1) + 'profiles/ppp/latest/{{lang}}/reference/codelists/#' + codelist
        return match.group()

    return re.sub(r'(://standard\.open-contracting\.org/)[^/]+/[^/]+/schema/codelists/#([a-z-]+)', replace, text)


profile_identifier = 'ppp'
repository_url = 'https://github.com/open-contracting-extensions/public-private-partnerships'

html_theme_options = {
    'display_version': True,
    'root_url': '/profiles/{}'.format(profile_identifier),
    'short_project': 'OCDS for PPPs',
    'copyright': copyright,
    'license_name': 'Apache License 2.0',
    'license_url': '{}/blob/HEAD/LICENSE'.format(repository_url),
    'repository_url': repository_url,
}

# The version of OCDS to patch.
standard_tag = '1__1__4'
standard_version = '1.1'

# Where the patched schemas will be deployed.
schema_base_url = 'https://standard.open-contracting.org{}/schema/{}/'.format(
    html_theme_options['root_url'], release.replace('-', '__').replace('.', '__'))

# The `LOCALE_DIR` from `config.mk`, plus the theme's locale.
locale_dirs = ['../locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]

gettext_compact = False

# The `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = '{}-'.format(profile_identifier)

# List the extension identifiers and versions that should be part of this profile. The extensions must be available in
# the extension registry: https://github.com/open-contracting/extension_registry/blob/master/extension_versions.csv
extension_versions = {
    'bids': 'v1.1.4',
    'budget': 'master',
    'budget_project': 'master',
    'charges': 'master',
    'documentation_details': 'master',
    'finance': 'master',
    'location': 'v1.1.4',
    'metrics': 'master',
    'milestone_documents': 'v1.1.4',
    'performance_failures': 'master',
    'process_title': 'v1.1.4',
    'qualification': 'master',
    'requirements': 'master',
    'risk_allocation': 'master',
    'shareholders': 'master',
    'signatories': 'master',
    'tariffs': 'master',
    'transaction_milestones': 'master',
    'ppp': 'master',
}


def setup(app):
    app.add_config_value('extension_versions', extension_versions, True)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True
    }, True)

    app.add_transform(AutoStructify)

    # The root of the repository.
    basedir = Path(os.path.realpath(__file__)).parents[1]
    # The `LOCALE_DIR` from `config.mk`.
    localedir = basedir / 'locale'

    language = app.config.overrides.get('language', 'en')

    headers = ['Title', 'Description', 'Extension']
    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = '{}schema'.format(gettext_domain_prefix)
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = '{}codelists'.format(gettext_domain_prefix)

    patched_dir = basedir / 'schema' / 'patched'
    profile_dir = basedir / 'schema' / 'profile'
    patched_build_dir = basedir / 'docs' / '_static' / 'patched'
    profile_build_dir = basedir / 'build' / language

    translate([
        # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
        (glob(str(patched_dir / '*-schema.json')), patched_build_dir, schema_domain),
        (glob(str(profile_dir / '*-schema.json')), profile_build_dir, schema_domain),
        # The glob patterns in `babel_ocds_codelist.cfg` should match these.
        (glob(str(patched_dir / 'codelists' / '*.csv')), patched_build_dir / 'codelists', codelists_domain),
        (glob(str(profile_dir / 'codelists' / '*.csv')), profile_build_dir / 'codelists', codelists_domain),
    ], localedir, language, headers, version=standard_version)

    # Copy the untranslated extension.json file.
    with (profile_dir / 'extension.json').open() as f:
        extension_json = f.read()
    with (profile_build_dir / 'extension.json').open('w') as f:
        f.write(extension_json)
