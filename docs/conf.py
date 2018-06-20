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
from collections import OrderedDict

import standard_theme
from ocds_documentation_support import translate_codelists, translate_schema
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinxcontrib.opendataservices import AutoStructifyLowPriority

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
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
source_suffix = '.md'
source_parsers = {
    '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Open Contracting Data Standard for Public Private Partnerships'
copyright = '2016-2017 Open Contracting Partnership'
author = 'Open Data Services / Open Contracting Partnership'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.rc'

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
html_static_path = ['../schema', '_static', 'examples']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
html_extra_path = ['../schema/consolidatedExtension']

# -- Local configuration --------------------------------------------------

locale_dirs = ['../locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]
gettext_compact = False
profile_identifier = 'ppp'
extension_versions = OrderedDict([
    ('bids', 'v1.1.3'),
    ('budget', 'master'),
    ('budget_project', 'master'),
    ('charges', 'master'),
    ('documentation_details', 'master'),
    ('finance', 'master'),
    ('location', 'v1.1.3'),
    ('metrics', 'master'),
    ('milestone_documents', 'v1.1.3'),
    ('performance_failures', 'master'),
    ('process_title', 'v1.1.3'),
    ('qualification', 'master'),
    ('requirements', 'master'),
    ('risk_allocation', 'master'),
    ('shareholders', 'master'),
    ('signatories', 'master'),
    ('tariffs', 'master'),
    ('transaction_milestones', 'master'),
])


def setup(app):
    app.add_config_value('extension_versions', extension_versions, True)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True
    }, True)

    app.add_transform(AutoStructify)
    app.add_transform(AutoStructifyLowPriority)

    basedir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
    localedir = os.path.join(basedir, 'locale')

    filenames = [
        'ppp-release-schema.json',
    ]

    directories = (
        ('compiledCodelists', 'docs/_static/codelists'),
        ('docs/extensions/codelists', 'docs/extensions/codelists_translated'),
    )

    language = app.config.overrides.get('language', 'en')
    translate_schema('ppp-schema', filenames, os.path.join(basedir, 'schema'), os.path.join(basedir, 'docs', '_static'), localedir, language)  # noqa
    for sourcedir, buildir in directories:
        translate_codelists('ppp-codelists', os.path.join(basedir, sourcedir), os.path.join(basedir, buildir), localedir, language)  # noqa
