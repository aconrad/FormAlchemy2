#!/bin/bash
rm .coverage .noseids
nosetests -v --with-id --with-coverage --cover-package=formalchemy2 -s
