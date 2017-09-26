# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from gcdt.gcdt_openapi import get_openapi_defaults, get_openapi_scaffold_min, \
    get_openapi_scaffold_max, validate_tool_config

from gcdt_tenkai import read_openapi


def test_scaffolding_default():
    spec = read_openapi()
    expected_defaults = {
        'defaults': {
            'log_group': '/var/log/messages',
            'settings_file': 'settings.json',
            'stack_output_file': 'stack_output.yml',
            'validate': True
        }
    }

    tenkai_defaults = get_openapi_defaults(spec, 'tenkai')
    assert tenkai_defaults == expected_defaults
    validate_tool_config(spec, {'tenkai': tenkai_defaults})


def test_scaffolding_sample_min():
    spec = read_openapi()
    expected_sample = {
        'codedeploy': {
            'applicationName': u'string',
            'deploymentConfigName': u'string',
            'deploymentGroupName': u'string'
        }
    }

    tenkai_sample = get_openapi_scaffold_min(spec, 'tenkai')
    assert tenkai_sample == expected_sample
    validate_tool_config(spec, {'tenkai': tenkai_sample})


def test_scaffolding_sample_max():
    spec = read_openapi()
    expected_sample = {
        'codedeploy': {
            'applicationName': 'string',
            'deploymentGroupName': 'string',
            'artifactsBucket': 'string',
            'deploymentConfigName': 'string'
        },

        'bundling': {
            'folders': {
                'folders': [{'source': './node_modules', 'target': './node_modules'}]
            },
            'zip': 'bundle.zip'
        },

        'defaults': {
            'validate': True,
            'log_group': '/var/log/messages',
            'stack_output_file': 'stack_output.yml',
            'settings_file': 'settings.json'
        }
    }

    tenkai_sample = get_openapi_scaffold_max(spec, 'tenkai')
    #print(tenkai_sample)
    assert tenkai_sample == expected_sample
    validate_tool_config(spec, {'tenkai': tenkai_sample})
