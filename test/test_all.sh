#!/bin/bash
rm .coverage
nosetests -v --with-id --with-coverage --cover-package=formalchemy2 -s
