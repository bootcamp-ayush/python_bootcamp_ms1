#!groovy

pipeline {
        options {
            buildDiscarder(logRotator(artifactDaysToKeepStr: '30', artifactNumToKeepStr: '5', daysToKeepStr: '30', numToKeepStr: '5'))
        }
        environment{
            PROJECT_NAME = 'python_bootcamp_ms1'
            VERSION = '1.0.0'
            NAMESPACE = 'python_bootcamp'
            DOCKER_REGISTRY_URL = ""
            DOCKER_REGISTRY = ''
            /*REGISTRY_ACCESS = credentials('sps-harbour-user')*/
            RELEASE_NAME = 'python_bootcamp_ms1'
            BRANCH =  sh(script: 'echo $BRANCH_NAME', , returnStdout: true).trim()

        }
        agent { docker 'python:3.8.0-alpine3.10' }
        stages {
            stage('Install Requirements') {
                steps {
                       sh '''
                        pip install -r requirements.txt
                       '''
                    }
                }

            stage('Unit tests') {
                steps {
                    sh '''
                    python -m pytest tests/unittests -s --junitxml='pyTests.xml' --alluredir='allure-results'
                    '''
                }
            }

            stage('Coverage') {
                steps {
                    sh '''
                    python -m pytest tests/unittests --cov=. --cov-config=pipelines/conf/.coveragerc --cov-report xml:coverage-reports/coverage.xml --cov-report html:coverage-reports --cov-report annotate:coverage-reports --cov-report term-missing
                    echo "**********************************************************"
                    cat ./coverage-reports/coverage.xml
                    echo "**********************************************************"
                    '''
                }
            }
        }
    }
